import { createContext, useContext } from 'react';

const useSettingsContext = () => useContext(SettingsContext)

export const SettingsContext = createContext();
export default useSettingsContext;