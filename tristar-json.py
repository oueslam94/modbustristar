from pyModbusTCP.client import ModbusClient
import time
import datetime
import webbrowser
import json

# TCP auto connect on modbus request, close after it

host= '10.0.0.21' #home 10.0.0.21   ES Lab 192.
port = 502
client = ModbusClient(host, port, timeout=10, unit_id=1, auto_open=True, auto_close=True)

# Define the State list
state = ['Start', 'Night Check', 'Disconnected', 'Night', 'Fault!', 'MPPT', 'Absorption', 'FloatCharge', 'Equalizing', 'Slave']
faults = ['no faults', 'overcurrent', 'FETs shorted', 'software bug', 'battery HVD', 'array HVD', 'settings switch changed', 'custom settings edit', 'RTS shorted', 'RTS disconnected', 'EEPROM rety limit', 'reserved', 'slave control timeout']
led = ['LED start', 'LED start 2', 'LED branch', 'fast green blink', 'slow green blink', 'green blink 1Hz', 'Green 80%', 'Green-Yellow 50%', 'yellow 20%','Yellow-Red 0%', 'blink red', 'red', 'R-Y-G error', 'R/Y-G error', 'R/G-Y error', ' HTD R-Y error', 'HVD R-G error', 'R/Y-G/Y error', 'G/Y/R error', 'G/Y/R x2']
# read registers. Start at 0 for convenience

values = {}


#url='tristar-status.html'

# battery sense voltage, filtered
while True:
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    # Grab all modbus data
    rr = client.read_input_registers(0,80)
    if rr == None: #in case the connection is not established or just testing UI
        values["Time"] = (st)
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
        values["Solar_Voltage"] = '...'
        values["Solar_Current"] = '...'
        values["Solar_Power"] = '...'

        with open('ReactApp/joesapp/src/Components/tristar.json', 'w') as fp:
            json.dump(values, fp)
        time.sleep(10)
    else:
        print(rr)
        # for all indexes, subtract 1 from what's in the manual
        V_PU_hi = rr[0]
        V_PU_lo = rr[1]
        I_PU_hi = rr[2]
        I_PU_lo = rr[3]

        V_PU = float(V_PU_hi) + float(V_PU_lo)
        I_PU = float(I_PU_hi) + float(I_PU_lo)

        v_scale = V_PU * 2**(-15)
        i_scale = I_PU * 2**(-15)
        p_scale = V_PU * I_PU * 2**(-17)

        #values start here
        battsV = rr[24] * v_scale
        battsSensedV = rr[26] * v_scale
        battsTargetV = rr[51] * v_scale
        battsI = rr[28] * i_scale
        arrayV = rr[27] * v_scale
        arrayI = rr[29] * i_scale
        battsW = float(battsV) * float(battsI)
        arrayW = float(arrayV) * float(arrayI)
        statenum = rr[50]
        hsTemp = rr[35]
        rtsTemp = rr[36]
        batTemp = rr[37]
        outPower = rr[58] * p_scale
        inPower = rr[59] * p_scale
        minVb_daily = rr[64] * v_scale
        maxVb_daily = rr[65] * v_scale
        minTb_daily = rr[71]
        maxTb_daily = rr[72]
        faultnum = rr[44]
        alarm1 = rr[46]
        alarm2 = rr[47]
        dipswitches = bin(rr[48])[::-1][:-2].zfill(8)
        led_state = rr[49]

    # Populate values
        values["Time"] = (st)
        values["Battery_SOC"] = (led[led_state])
        values["Battery_Voltage"] = (battsV)
        values["Battery_Sensed_Voltage"] = (battsSensedV)
        values["Battery_Target_Voltage"] = (battsTargetV)
        values["Battery_Current"] = (battsI)
        values["Charge_State"] = (state[statenum])
        values["Battery_Power"] = (battsW)
        values["Battery_Voltage"] = (battsV)
        values["RTS_Temp"] = (rtsTemp)
        values["Heatsink_Temp"] = (hsTemp)
        values["Battery_Temp"] = (batTemp)
        values["Solar_Voltage"] = (arrayV)
        values["Solar_Current"] = (arrayI)
        values["Solar_Power"] = (arrayW)

        with open('tristar.json', 'w') as fp:
            json.dump(values, fp)

        time.sleep(10)

    '''
        f = open('tristar.js', 'w')
        newdata = json.dumps(values)
        print (newdata)
        message = """

            <script type="text/javascript">
            <p className="App-intro">
              Below are the details for your system. {}, {}, {}
            </p>
            </script>
        """
        .format(st, led[led_state], battsV, battsSensedV, battsI, state[statenum], battsW, rtsTemp, hsTemp, arrayV, arrayI, arrayW)
        f.write(message)
        f.close()
    '''
