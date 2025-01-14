export interface ISysInfoTemperatures {
    name: string;
    temperatures?: ITemperatures;
    fans?: string[];
}

export interface ITemperatures {
    current: string;
    high: string;
    critical: string;
}
