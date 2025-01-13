export interface ISysInfo {
    cpu: ICpu;
    memory: IMemory;
    disk: IDisk;
    network: INetwork;
}

export interface INetwork {
    throughput: IThroughput;
    connections: number;
}

export interface IThroughput {
    bytes_sent: number;
    bytes_recv: number;
}

export interface IDisk {
    usage: number;
    read_bytes: number;
    write_bytes: number;
    temperature: ITemperature2;
}

export interface ITemperature2 {
}

export interface ISysInfoMemory {
    memory: IMemory;
    swap: ISwap;
}

export interface ISwap {
    usage: number;
    total: number;
    used: number;
    free: number;
    sin: number;
    sout: number;
}

export interface IMemory {
    total: number;
    available: number;
    usage: number;
    other: IMemoryOther;
}

export interface IMemoryOther {
    used: number;
    free: number;
    active: number;
    inactive: number;
    buffers: number;
    cached: number;
    shared: number;
    slab: number;
}

export interface ICpu {
    usage: number;
    count: number;
    load: number[];
    temperature: ITemperature;
}

export interface ITemperature {
    error: string;
}
