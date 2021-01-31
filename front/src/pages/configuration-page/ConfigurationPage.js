import React, { useEffect } from 'react'
import { func, string } from 'prop-types';

import './ConfigurationPage.scss';
import useSettingsContext from '../../contexts/SettingsContext';

const ConfigurationPage = () => {
    const {isDark, toggleDarkTheme} = useSettingsContext();

    useEffect(() => {
        console.log("on mount settings page");
        return () => console.log("on destroy settings page")
    }, [isDark]);
    
    return (
        <div className="page">
            <div className="row">
                <h1>Settings</h1>
            </div>
            <div className="row">
                <p>Dark theme</p>
                <label className="switch">
                    <input type="checkbox" onChange={toggleDarkTheme} checked={isDark} />
                    <span className="slider"></span>
                </label>
            </div>
        </div>
    )
}

ConfigurationPage.prototype = {
    state: string.isRequired,
    callback: func.isRequired,
}

export default ConfigurationPage;