import {defineStore} from "pinia";

export const useHome = defineStore('home', {
    state: () => ({
        // 选择的后端服务器ip
        selectIP: ''
    }),
    actions: {
        setSelectIP(payload: string) {
            this.selectIP = payload
        }
    },
    getters: {
        getSelectIP: (state) => state.selectIP
    },
    persist: true
})
