import React, { Component } from 'react';
import Table from './Components/Table'
import logo from './logo.svg';
import './App.css';
import './tristar.json'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">ModBox Details</h1>
        </header>
        <p className="App-intro">
        <Table/>
        </p>
          <p></p><p></p>
          For more details go to: <a href="http://www.ModEnergySystems.com"> ModBox</a>
          <p></p>
         </div>

    );
  }
}


export default App;
