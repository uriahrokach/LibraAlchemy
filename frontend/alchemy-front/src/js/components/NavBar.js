import React from 'react';
import '../../css/Navbar.css';
import { useLocation } from 'react-router';
import logo from '../../icons/Libra7_Website.png';
import {GiMagicPotion, GiBookshelf, GiChemicalDrop} from 'react-icons/gi';

const pageNames = {
  '/': {name: 'רקיחת שיקוי', icon: <GiMagicPotion size='40px' />},
  '/potion-list': {name: 'רשימת השיקויים', icon: <GiBookshelf size='40px' />}, 
  '/create-potion': {name: 'יצירת שיקוי', icon: <GiChemicalDrop size='40px' />},
}

const Navbar = () => {
  const location = useLocation();

  return (
    <header className='navbar-background'>
      <img src={logo} alt='logo' />
      <div className='navbar-bar'>
        <div className='navbar-main'>
          {pageNames[location.pathname].icon}
          <h4>{pageNames[location.pathname].name}</h4>
        </div>
        <div className='navbar-nav'>
          <a href='/create-potion'>יצירת שיקוי</a>
          <a href='/'>רקיחת שיקוי</a>
          <a href='/potion-list'>רשימת השיקויים</a>
        </div>
      </div>
    </header>
  );
};

export default Navbar;