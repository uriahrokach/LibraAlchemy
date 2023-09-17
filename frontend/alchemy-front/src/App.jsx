import './App.css';

import React from 'react';

import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import Alchemist from './js/pages/Alchemist';
import { CreatePotion } from './js/pages/CreatePotion';
import {PotionList} from './js/pages/PotionList';
import Navbar from './js/components/NavBar';

const App = () => {

  return (
    <div className="App">
      <ToastContainer position='bottom-right' newestOnTop={true} />
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Alchemist} />
          <Route path='/potion-list' component={PotionList} />
          <Route path='/create-potion' component={CreatePotion} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;