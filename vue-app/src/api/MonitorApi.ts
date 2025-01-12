import request from "@/utils/request.ts";
import {ICpu, IMemory} from "@/interface/ISysInfo.ts";

const MonitorApi = {
    /**
     * 获取cpu信息
     */
    sysCpuInfo() {
        return request<ICpu>({
            url: "/get_cpu_info",
            method: "GET"
        })
    },
    /**
     * 获取内存信息
     */
    sysMemoryInfo() {
        return request<IMemory>({
            url: "/get_memory_info",
            method: "GET"
        })
    },
    /**
     * 获取磁盘列表
     */
    sysDiskList() {
        return request<string[]>({
            url: "/list_disks",
            method: "GET"
        })
    },
    /**
     * 获取磁盘信息
     */
    sysDiskInfo(path: string) {
        return request<ISysInfoDiskInfo>({
            url: "/get_disk_info",
            method: "GET",
            params: {
                path
            }
        })
    }
}

export default MonitorApi
