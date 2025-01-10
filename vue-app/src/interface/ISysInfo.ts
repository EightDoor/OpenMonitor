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
export interface IMemory {
    usage: number;
    swap_usage: number;
}
export interface ICpu {
    usage: number;
    load: number[];
    temperature: ITemperature;
}
export interface ITemperature {
    error: string;
}
