import { useEffect, useState } from 'react';

const useDarkMode = () => {
  const [theme, setTheme] = useState(false);
  const [componentMounted, setComponentMounted] = useState(false);

  const setMode = mode => {
    window.localStorage.setItem('theme', mode)
    setTheme(mode);
  }

  const toggleTheme = () => {
    setMode(!theme);
  };

  useEffect(() => {
    const mode = window.localStorage.getItem('theme');
    if (mode) {
      setTheme(mode === 'true');
    } else {
      setTheme(false);
    }
    setComponentMounted(true);
  }, [theme]);

  return [theme, toggleTheme, componentMounted];
};

export default useDarkMode;