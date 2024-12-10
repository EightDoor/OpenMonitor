// 定义getTime和padMs函数，保持原有功能但增加类型注解
function getTime(): string {
    const date = new Date();
    return `${date.toLocaleTimeString('en-US', {
        hour12: false,
    })}.${padMs(date.getMilliseconds())}`;
}

function padMs(ms: number): string {
    const len = ms.toString().length;
    let ret: string;
    switch (len) {
        case 1:
            ret = `00${ms}`;
            break;
        case 2:
            ret = `0${ms}`;
            break;
        default:
            ret = ms.toString();
            break;
    }
    return ret;
}

// 定义Log类并使用typescript的类和方法特性
export default class Log {
    private mark = 'cloudBased';
    private prefix = '';

    constructor(prefix?: string) {
        this.prefix = prefix || '';
    }

    // 使用void明确此方法无返回值，同时使用public指定访问权限（默认可省略，但显式声明更清晰）
    public setPrefix(param: any[]): void { // 使用any[]是因为arguments类型在TS中不易处理，可根据实际情况细化类型
        let prefix = `${getTime()} [${this.mark}`;
        if (this.prefix.length > 0) {
            prefix += `.${this.prefix}]:`;
        } else {
            prefix += ']:';
        }
        param.unshift(prefix);
    }

    public log(...params: any[]): void { // 使用rest参数替代Array.from(arguments)
        this.setPrefix(params);
        console.log(...params); // 使用扩展运算符
    }

    public debug(...params: any[]): void { // 使用rest参数替代Array.from(arguments)
        this.setPrefix(params);
        console.log(...params); // 使用扩展运算符
    }


    public info(...params: any[]): void { // 使用rest参数替代Array.from(arguments)
        this.setPrefix(params);
        console.log(...params); // 使用扩展运算符
    }


    public warn(...params: any[]): void {
        this.setPrefix(params);
        console.warn(...params);
    }

    public error(...params: any[]): void {
        this.setPrefix(params);
        console.error(...params);
    }
}
