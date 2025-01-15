import request from "@/utils/request.ts";
import {IAverageLoad, ICpu, IDiskHealth, IMemory} from "@/interface/ISysInfo.ts";
import {ISysInfoDiskInfo} from "@/interface/ISysInfoDisk.ts";
import {ISysInfoIOStatistics} from "@/interface/ISysInfoIOStatistics.ts";
import {ISysInfoTemperatures} from "@/interface/ISysInfoTemperatures.ts";

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
     * cpu平均负载
     */
    sysAverageLoad() {
        return request<IAverageLoad>({
            url: "/average_load",
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
    },
    /**
     * 获取磁盘IO
     */
    sysDiskIO() {
        return request({
            url: "/get_disk_io",
            method: "GET",
        })
    },
    /**
     * 获取网络统计信息
     */
    networkTrafficStatistics() {
        return request<ISysInfoIOStatistics>({
            url: "/network_traffic_statistics",
            method: "GET",
        })
    },
    /**
     * 获取硬件温度
     */
    getTemp() {
        return request<ISysInfoTemperatures[]>({
            url: "/get_temp",
            method: "GET"
        })
    },
    /**
     * 磁盘健康检查
     */
    getDiskHealth(disk: string) {
        return request<IDiskHealth>({
            url: "/get_disk_smart_status",
            method: "GET",
            params: {
                disk
            }
        })
    }
}

export default MonitorApi
