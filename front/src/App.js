import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import { lightTheme, darkTheme } from './theme';
import { GlobalStyles } from './global';

import './App.scss';
import useDarkMode from './hooks/useDarkMode';
import Navigation from './common/navigation/Navigation';
import ColorPage from './pages/color-page/ColorPage';
import ConfigurationPage from './pages/configuration-page/ConfigurationPage';
import {SettingsContext} from './contexts/SettingsContext';
import route from './common/navigation/route';
import SnakePage from './pages/snake-page/SnakePage';

const App = () => {
  const [isDark, toggleDarkTheme] = useDarkMode();

  return (
    <SettingsContext.Provider value={{isDark, toggleDarkTheme}}>
      <ThemeProvider theme={isDark ? darkTheme : lightTheme}>
        <GlobalStyles />
        <Router>
          <div className="App">
            <Navigation></Navigation>

            <Switch>
              <Route path={route.home} exact>
                <ColorPage />
              </Route>
              <Route path={route.snake}>
                <SnakePage />
              </Route>
              <Route path={route.settings}>
                <ConfigurationPage />
              </Route>
            </Switch>
          </div>
        </Router>
      </ThemeProvider>
    </SettingsContext.Provider>
  );
}

export default App;
