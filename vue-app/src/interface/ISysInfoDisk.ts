interface ISysInfoDiskInfo {
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
