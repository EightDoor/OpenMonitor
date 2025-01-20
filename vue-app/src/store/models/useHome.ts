import {defineStore} from "pinia";
import {DomainItem} from "@/views/home/components/Settings/Host.vue";
import StoreUtil from "@/utils/StoreUtil.ts";
import Constant from "@/utils/Constant.ts";

export const useHome = defineStore('homeStore', {
    state: () => {
        return {
            // 选择的后端服务器ip
            selectIP: '',
            serverIps: [] as DomainItem[],
        }
    },
    actions: {
        setSelectIP(payload: string) {
            this.selectIP = payload
            StoreUtil.set(Constant.selectIP, payload)
        },
        setServerIps(payload: DomainItem[]) {
            this.serverIps = payload;
            StoreUtil.set(Constant.serverIPS, payload)
        }
    },
    getters: {
        getSelectIP: (state) => state.selectIP,
        getServerIps: (state) => state.serverIps
    }
})
