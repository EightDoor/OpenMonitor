const Utils = {
    /**
     * 字节转换为MB
     * @param bytes
     */
    bytesToMB(bytes, digits = 0) {
        if (isNaN(bytes) || bytes < 0) {
            throw new Error("请输入一个有效的字节数")
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
        const GB = Utils.bytesToMB(bytes, digits) / 1024
        return GB.toFixed(digits)
    }
}

export default Utils
