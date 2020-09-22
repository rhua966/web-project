import React, { Component } from 'react'
// import { BrowserRouter, Router, Switch } from 'react-router-dom'
// import { v4 as uuidv4 } from 'uuid'
// import Home from './components/Home'
// import About from './components/About'
import Navigation from './components/Navigation'
import Main from './Main'
// import ProductList from './components/ProductList'



class App extends Component {
  
  render() {
    return (
      <div className="App">
        <Navigation />
        <Main />
      </div>
    )
  }
}

export default App;
