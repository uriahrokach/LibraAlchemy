import './App.css';

import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Alchemist from './js/pages/Alchemist';
import {PotionList} from './js/pages/PotionList';
import {Settings} from './js/pages/Settings';
import Navbar from './js/components/NavBar';

const App = () => {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Switch>
          <Route path='/' exact component={Alchemist} />
          <Route path='/potion-list' component={PotionList} />
          <Route path='/settings' component={Settings} />
          <Route path='/create' component={null} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;