import React, { useEffect } from 'react'
import './ColorPage.scss';

const ColorPage = () => {

    useEffect(() => {
        console.log("on mount color page");
        return () => console.log("on destroy color page")
    });

    return <div className="page">
        <div className="row">
            <h1>Color Wheel</h1>
        </div>
    </div>
}

export default ColorPage;