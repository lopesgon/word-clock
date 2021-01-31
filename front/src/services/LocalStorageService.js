const setKey = (key, value) => window.localStorage.setItem(key, value)
const getKey = (key) => window.localStorage.getItem(key)

const StorageService = {
    setKey,
    getKey
}

export default StorageService;