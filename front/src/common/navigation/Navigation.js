import React from 'react';
import './Navigation.scss';
import { Link } from 'react-router-dom';
import route from './route';

const Navigation = () => {
    return <nav id="navbar">
        <div className="icons">
            <Link to={route.home}>
                <img src="/icons/color-wheel.svg" alt="Color wheel" />
            </Link>
            <Link to={route.snake}>
                <img src="/icons/snake.svg" alt="Snake" />
            </Link>
            <Link to={route.settings}>
                <img src="/icons/settings.svg" alt="Settings" />
            </Link>
        </div>
    </nav>
}

export default Navigation;