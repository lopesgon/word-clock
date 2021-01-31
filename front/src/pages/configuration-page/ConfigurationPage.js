import React, { useEffect } from 'react'
import { func, string } from 'prop-types';

import './ConfigurationPage.scss';

const ConfigurationPage = ({state, callback}) => {

    useEffect(() => {
        console.log("ConfPage useEffect");
    });

    return (
        <div className="page">
            <div className="row">
                <h1>Settings</h1>
            </div>
            <div className="row">
                <p>Dark theme</p>
                <label className="switch">
                    <input type="checkbox" onChange={callback} checked={state} />
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