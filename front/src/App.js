import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';
import { lightTheme, darkTheme } from './theme';
import { GlobalStyles } from './global';

import './App.scss';
import useDarkMode from './hooks/useDarkMode';
import Navigation from './common/navigation/Navigation';
import ColorPage from './pages/color-page/ColorPage';
import ConfigurationPage from './pages/configuration-page/ConfigurationPage';

const App = () => {
  const [theme, setTheme] = useState(false);

  const themeCallback = () => {
    setTheme(!theme);
  }

  useEffect(() => {
    console.log("app useEffect");
  });

  return (
    <ThemeProvider theme={theme ? darkTheme : lightTheme}>
      <GlobalStyles />
      <Router>
        <div className="App">
          <Navigation></Navigation>

          <Switch>
            <Route path="/" exact>
              <ColorPage />
            </Route>
            <Route path="/configuration">
              <ConfigurationPage state={theme} callback={themeCallback} />
            </Route>
          </Switch>
        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;
