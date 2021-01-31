import React from 'react';
import './Navigation.scss';
import { Link } from 'react-router-dom';
import WheelIcon from '../../icons/color-wheel.svg';
import SettingsIcon from '../../icons/settings.svg';


const Navigation = () => {
    return <nav id="navbar">
        <div className="icons">
            <Link to="/">
                <img src={WheelIcon} alt="Color wheel" />
            </Link>
            <Link to="/configuration">
                <img src={SettingsIcon} alt="Settings" />
            </Link>
        </div>
    </nav>
}

export default Navigation;