from pyModbusTCP.client import ModbusClient
import time
import datetime
import webbrowser
import json
import hwconfig

# TCP auto connect on modbus request, close after it
client = ModbusClient(hwconfig.host, hwconfig.port, timeout=10, unit_id=1, auto_open=True, auto_close=True)

# Define the State list
state = ['Start', 'Night Check', 'Disconnected', 'Night', 'Fault!', 'MPPT', 'Absorption', 'FloatCharge', 'Equalizing', 'Slave']
faults = ['no faults', 'overcurrent', 'FETs shorted', 'software bug', 'battery HVD', 'array HVD', 'settings switch changed', 'custom settings edit', 'RTS shorted', 'RTS disconnected', 'EEPROM rety limit', 'reserved', 'slave control timeout']
led = ['LED start', 'LED start 2', 'LED branch', 'Equalization State', 'Absorption States', 'Floar State', '80%+ Green', '60%+ Green-Yellow', '35%+ yellow','0%+ Yellow-Red', 'blink red', '<0% red', 'Dip switch changed, restart', 'Battery Over-Current', 'R/G-Y error', ' High Temp Defence', 'HHigh Voltage Defence', 'R/Y-G/Y error', 'G/Y/R error', 'G/Y/R x2']
flags_daily = ['reset detected', 'equalize triggered', 'enter float', 'alarm occured', 'fault occured']
# read registers. Start at 0 for convenience

values = {}


#url='tristar-status.html'

# battery sense voltage, filtered
while True:
    ts = time.time()
    sd = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

    # Grab all modbus data
    rr = client.read_input_registers(0,80)
    if rr == None: #in case the connection is not established or just testing UI
        # values["Date"] = (sd)
        # valies["Time"] = (st)
        values["Connection"] = 'Offline'
        values["Battery_SOC"] = '...'
        values["Battery_Voltage"] = '...'
        values["Battery_Sensed_Voltage"] = '...'
        values["Battery_Target_Voltage"] = '...'
        values["Battery_Current"] = '...'
        values["Charge_State"] = '...'
        values["Battery_Power"] = '...'
        values["Battery_Voltage"] = '...'
        values["RTS_Temp"] = '...'
        values["Heatsink_Temp"] = '...'
        values["Battery_Temp"] = '...'
        values["RTS_TempF"] = '...'
        values["Heatsink_TempF"] = '...'
        values["Battery_TempF"] = '...'
        values["Solar_Voltage"] = '...'
        values["Solar_Current"] = '...'
        values["Solar_Power"] = '...'
        values["Faults"] = '...'
        values["Alarms"] = '...'
        values["Produced_Today"] = '...'
        values["Daily_Flags"] = '...'


        with open('ReactApp/joesapp/src/Components/tristar.json', 'w') as fp:
            json.dump(values, fp)
        time.sleep(10)
    else:
        print(rr)
        # for all indexes, subtract 1 from what's in the manual
    #Scales
        V_PU_hi = rr[0]
        V_PU_lo = rr[1]
        I_PU_hi = rr[2]
        I_PU_lo = rr[3]

        V_PU = float(V_PU_hi) + float(V_PU_lo)
        I_PU = float(I_PU_hi) + float(I_PU_lo)

        v_scale = V_PU * 2**(-15)
        i_scale = I_PU * 2**(-15)
        p_scale = V_PU * I_PU * 2**(-17)

    #Battery
        battsV = rr[24] * v_scale
        battsSensedV = rr[26] * v_scale
        battsTargetV = rr[51] * v_scale
        battsI = rr[28] * i_scale
        battsW = float(battsV) * float(battsI)
    #Solar Array
        arrayV = rr[27] * v_scale
        arrayI = rr[29] * i_scale
        arrayW = float(arrayV) * float(arrayI)
        outPower = rr[58] * p_scale
        inPower = rr[59] * p_scale
    #Temperatures in C
        hsTemp = rr[35]
        rtsTemp = rr[36]
        batTemp = rr[37]
    #Logs & Status
        statenum = rr[50]
        minVb_daily = rr[64] * v_scale
        maxVb_daily = rr[65] * v_scale
        minTb_daily = rr[71]
        maxTb_daily = rr[72]
        whc_daily = rr[68]
        flags_dailynum = rr[69]
        faultnum = rr[44]
        alarm1 = rr[46]
        alarm2 = rr[47]
        dipswitches = bin(rr[48])[::-1][:-2].zfill(8)
        led_state = rr[49]

    # Populate values
        values["Date"] = (sd)
        values["Time"] = (st)
        values["Connection"] = 'Online'
    # Battery
        values["Battery_SOC"] = (led[led_state])
        values["Battery_Voltage"] = round((battsV),2)
        values["Battery_Sensed_Voltage"] = round((battsSensedV),2)
        values["Battery_Target_Voltage"] = round((battsTargetV),2)
        values["Battery_Current"] = round((battsI),2)
        values["Charge_State"] = (state[statenum])
        values["Battery_Power"] = round((battsW),2)
    # Temperatures in C & F
        values["RTS_Temp"] = round((rtsTemp),2)
        values["Heatsink_Temp"] = round((hsTemp),2)
        values["Battery_Temp"] = round((batTemp),2)
        values["RTS_TempF"] = round(((rtsTemp * 1.8) + 32),1)  #(Celcius - 32) * 5.0/9.0
        values["Heatsink_TempF"] = round(((hsTemp * 1.8) + 32),1)
        values["Battery_TempF"] = round(((batTemp * 1.8) + 32),1)
    # Solar Array
        values["Solar_Voltage"] = round((arrayV),2)
        values["Solar_Current"] = round((arrayI),2)
        values["Solar_Power"] = round((arrayW),2)
        values["Produced_Today"] = round((whc_daily),1)
    # Logs & Status
        values["Faults"] = (faults[faultnum])
        values["Alarms"] = (alarm1, alarm2)
        values["Daily_Flags"] = (flags_dailynum)

        with open('ReactApp/joesapp/src/Components/tristar.json', 'w') as fp:
            json.dump(values, fp)

        time.sleep(10)

