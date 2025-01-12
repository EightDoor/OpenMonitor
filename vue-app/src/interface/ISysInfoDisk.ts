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
    read_count: number;
    write_count: number;
    read_latency: number;
    write_latency: number;
    read_bytes: number;
    write_bytes: number;
}
