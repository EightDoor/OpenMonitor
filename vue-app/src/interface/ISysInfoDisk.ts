export interface ISysInfoDiskInfo {
    total: number;
    used: number;
    free: number;
    usage: number;
    temperature: any;
    device?: string;
    path?: string;
    fs_type?: string;
    options?: string;
}

export interface ISysInfoDiskIO {
    read_bytes: number;
    write_bytes: number;
    read_count: number;
    write_count: number;
    read_time?: number;
    write_time: ? number;
    busy_time?: number;
    read_merged_count?: number;
    write_merged_count?: number;
}
