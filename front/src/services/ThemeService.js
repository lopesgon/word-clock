import LocalStorageService from "./LocalStorageService";

const THEME_STORAGE_KEY = 'theme';

const getTheme = () => LocalStorageService.getKey(THEME_STORAGE_KEY) === 'true'
const setTheme = (value) => LocalStorageService.setKey(THEME_STORAGE_KEY, value)

const ThemeService = {
    getTheme,
    setTheme
}

export default ThemeService;