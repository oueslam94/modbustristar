import React from 'react'
class Table extends React.Component {
  constructor(props){
    super(props)
    this.state = {
  }
  this.updateAur = this.updateAur.bind(this)


}

  componentDidMount() {
    // componentDidMount is called by react when the component
    // has been rendered on the page. We can set the interval here:
    this.updateAur()
    // this.timer = setInterval(this.updateAur, 500);
  }

  componentWillUnmount() {

    // This method is called immediately before the component is removed
    // from the page and destroyed. We can clear the interval here:
    // clearInterval(this.timer);
  }

  updateAur = () => {
    var config = require('./tristar.json');
    console.log(config,this.state)
    this.setState({...config})
  }

  render() {
    return ( <
      div >
      {this.state.Time}
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
      td > {this.state.Battery_SOC} < /td> <
      /tr> <
      tr >
      <
      td > Battery Voltage < /td> <
      td > {this.state.Battery_Voltage} < /td> <
      /tr> <
      tr >
      <
      td > Target Voltage < /td> <
      td > {this.state.Battery_Target_Voltage} < /td> <
      /tr> <
      tr >
      <
      td > Charge Current < /td> <
      td > {this.state.Battery_Current} < /td> <
      /tr> <
      tr >
      <
      td > Charge State < /td> <
      td > {this.state.Charge_State} < /td> <
      /tr> <
      tr >
      <
      td > Output Power < /td> <
      td > {this.state.Battery_Power} < /td> <
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
      td > {this.state.Battery_Temp} < /td> <
      /tr> <
      tr >
      <
      td > Heat Sink < /td> <
      td > {this.state.Heatsink_Temp} < /td> <
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
      td > {this.state.Solar_Voltage} < /td> <
      /tr> <
      tr >
      <
      td > Array Current < /td> <
      td > {this.state.Solar_Current} < /td> <
      /tr> <
      tr >
      <
      td > Array Power < /td> <
      td > {this.state.Solar_Power} < /td> <
      /tr> <
      /table> <
      /div>
    )
  }
}
export default Table
