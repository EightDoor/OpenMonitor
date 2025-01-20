const StoreUtil = {
    set(key: string, value: any) {
        localStorage.setItem(key, JSON.stringify(value))
    },
    get(key: string) {
        const result = localStorage.getItem(key)
        if (result) {
            return JSON.parse(result)
        }
        return '';
    },
    removeKey(key: string) {
        localStorage.removeItem(key)
    }
}

export default StoreUtil
