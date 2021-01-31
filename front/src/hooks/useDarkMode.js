import { useState } from 'react';
import ThemeService from '../services/ThemeService';

const useDarkMode = () => {
  const [isDark, setIsDark] = useState(ThemeService.getTheme());

  const toggleDarkTheme = () => {
    ThemeService.setTheme(!isDark)
    setIsDark(!isDark);
  };
  
  return [isDark, toggleDarkTheme];
};

export default useDarkMode;