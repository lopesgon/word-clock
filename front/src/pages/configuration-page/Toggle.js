import './Toggle.scss';

const Toggle = ({ isToggled, toggleCallback }) => {
    return (
        <label className="switch">
            <input type="checkbox" onChange={toggleCallback} checked={isToggled} />
            <span className="slider"></span>
        </label>
    )
}

export default Toggle;