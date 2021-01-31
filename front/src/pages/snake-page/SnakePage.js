import React, { useEffect } from 'react'
import './SnakePage.scss';

const SnakePage = () => {

    useEffect(() => {
        console.log("on mount snake page");
        return () => console.log("on destroy snake page")
    });

    return <div className="page">
        <div className="row">
            <h1>Snake Page</h1>
        </div>
    </div>
}

export default SnakePage;