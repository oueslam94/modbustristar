import React, { Component } from 'react';
import Table from './Components/Table'
import logo from './logo.svg';
import logowide from './logo-wide.svg';
import './App.css';
import './tristar.json'

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logowide} className="App-logo" alt="logo" />
        </header>
        <p className="App-intro">
        <Table/>
        </p>
        <p></p><p></p>
        <a href="http://www.ModEnergySystems.com">
        <img src={logo} className="App-logo2" alt="logo" />
        <p></p>Modular Energy Systems</a>
        <p>Technical Support: </p>
        <p>510 907 9804</p>
        <p><a href="mailto:info@ModEnergySystems.com">info@ModEnergySystems.com</a>  </p>
        </div>

    );
  }
}


export default App;
