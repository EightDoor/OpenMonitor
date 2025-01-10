import request from "@/utils/request.ts";
import {ICpu, ISysInfo} from "@/interface/ISysInfo.ts";

const MonitorApi = {
    /**
     * 获取cpu信息
     */
    sysCpuInfo() {
        return request<ICpu>({
            url: "/get_cpu_info",
            method: "GET"
        })
    }
}

export default MonitorApi
