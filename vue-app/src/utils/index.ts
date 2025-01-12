const Utils = {
    /**
     * 字节转换为MB
     * @param bytes
     */
    bytesToMB(bytes, digits = 0) {
        if (isNaN(bytes) || bytes < 0) {
            return 0
        }
        const MB = bytes / (1024 * 1024)
        return MB.toFixed(digits)
    },
    /**
     * MB转GB
     * @param bytes
     * @param digits
     */
    mbToGB(bytes, digits = 2) {
        if (bytes === 0) {
            return 0
        } else {
            const GB = Utils.bytesToMB(bytes, digits) / 1024
            return GB.toFixed(digits)
        }
    },
    /**
     * 将字节数转换为可读的 KB, MB, GB 格式
     * @param {number} bytes - 字节数
     * @param {number} decimals - 保留的小数位数，默认是 2
     * @returns {string} 格式化后的字符串
     */
    formatBytes(bytes, decimals = 2) {
        if (bytes === 0) return '0 Bytes'; // 如果字节数为 0

        const k = 1024; // 1 KB = 1024 Bytes
        const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']; // 单位
        const i = Math.floor(Math.log(bytes) / Math.log(k)); // 根据字节数选择单位

        // 计算大小并保留指定小数位数
        const formattedSize = parseFloat((bytes / Math.pow(k, i)).toFixed(decimals));

        return `${formattedSize} ${sizes[i]}`; // 返回带单位的字符串
    }
}

export default Utils
