import StoreUtil from "@/utils/StoreUtil.ts";
import Constant from "@/utils/Constant.ts";
import store from '@/store/index.ts';

import {useHome} from "@/store/models/useHome.ts";

const homeStore = useHome(store)

const BusinessUtil = {
    initStorage() {
        const selectIP = StoreUtil.get(Constant.selectIP)
        homeStore.setSelectIP(selectIP)
        const serverIPS = StoreUtil.get(Constant.serverIPS)
        homeStore.setServerIps(serverIPS)
    },
}

export default BusinessUtil
