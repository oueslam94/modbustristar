import React from 'react'
import { get, put } from 'axios'

class Table extends React.Component {
  constructor(props){
    super(props)
    this.state = {
  }
  this.updatedata = this.updatedata.bind(this)


}

  componentDidMount() {
    // componentDidMount is called by react when the component
    // has been rendered on the page. We can set the interval here:
    this.updatedata()
    this.timer = setInterval(this.updatedata, 2000);
  }

  componentWillUnmount() {

    // This method is called immediately before the component is removed
    // from the page and destroyed. We can clear the interval here:
    // clearInterval(this.timer);
  }

  updatedata = () => {
    // var config = require('./tristar.json');
    let uri= 'http://localhost:5000/rawdata';
    get(uri)
    .then((payload) => {
      console.log(payload,this.state)
    this.setState({...payload.data})
  })
  }

  render() {
    return ( <
      div ><
      p className = "time" >
      LAST CALL: {this.state.Date} at {this.state.Time}<
      /p >
      <
      table >
      <
      tr >
      <
      th colspan = "2" > Battery Details < /th> <
      /tr> <
      tr >
      <
      td > Battery State of Charge < /td> <
      td > {this.state.Battery_SOC} % < /td> <
      /tr> <
      tr >
      <
      td > Battery Voltage < /td> <
      td > {this.state.Battery_Voltage} V < /td> <
      /tr> <
      tr >
      <
      td > Target Voltage < /td> <
      td > {this.state.Battery_Target_Voltage} V< /td> <
      /tr> <
      tr >
      <
      td > Charge Current < /td> <
      td > {this.state.Battery_Current} A< /td> <
      /tr> <
      tr >
      <
      td > Charge State < /td> <
      td > {this.state.Charge_State} < /td> <
      /tr> <
      tr >
      <
      td > Output Power < /td> <
      td > {this.state.Battery_Power} W< /td> <
      /tr> <
      /table> <
      p > < /p> <
      table className = "table" >
      <
      tr >
      <
      th colspan = "2" > Temperatures < /th> <
      /tr> <
      tr >
      <
      td > Battery < /td> <
      td > {this.state.Battery_TempF} °F< /td> <
      /tr> <
      tr >
      <
      td > Heat Sink < /td> <
      td > {this.state.Heatsink_TempF} °F< /td> <
      /tr> <
      /table> <
      p > < /p> <
      table className = "table" >
      <
      tr >
      <
      th colspan = "2" > Solar PV < /th> <
      /tr> <
      tr >
      <
      td > Array Voltage < /td> <
      td > {this.state.Solar_Voltage} V< /td> <
      /tr> <
      tr >
      <
      td > Array Current < /td> <
      td > {this.state.Solar_Current} A< /td> <
      /tr> <
      tr >
      <
      td > Array Power < /td> <
      td > {this.state.Solar_Power} W< /td> <
      /tr> <
      tr >
      <
      td > Energy Today < /td> <
      td > {this.state.Produced_Today} Wh< /td> <
      /tr> <
      /table> <
      p > < /p> <
      table className = "table" >
      <
      tr >
      <
      th colspan = "2" > Flags & Warnings < /th> <
      /tr> <
      tr >
      <
      td > Daily Flags < /td> <
      td > {this.state.flags_daily} < /td> <
      /tr> <
      tr >
      <
      td > Faults < /td> <
      td > {this.state.Faults} < /td> <
      /tr> <
      tr >
      <
      td > Alarms < /td> <
      td > {this.state.Alarms} < /td> <
      /tr> <
      /table><
      /div>
    )
  }
}
export default Table
