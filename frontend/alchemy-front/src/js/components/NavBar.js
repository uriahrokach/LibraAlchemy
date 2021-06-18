import React from 'react';
import '../../css/Navbar.css';
import logo from '../../icons/Libra7_Website.png';
import {ReactComponent as PotionIcon} from '../../icons/serum.svg';

const Navbar = () => {
  return (
    <header className='navbar-background'>
      <img src={logo} alt='logo' />
      <div className='navbar-bar'>
        <div className='navbar-main'>
          <PotionIcon className='navbar-icon' />
          <h3>Hello</h3>
        </div>
        <div className='navbar-nav'>
          <a href='/settings'>יצירת שיקוי</a>
          <a href='/potion'>רקיחת שיקוי</a>
          <a href='/potion-list'>רשימת השיקויים</a>
        </div>
      </div>
    </header>
  );
};

export default Navbar;