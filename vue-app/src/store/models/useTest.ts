import {defineStore} from "pinia";

export const useTestCount = defineStore('useTestCount', {
    state: () => {
        return {
            count: 0
        }
    },
    actions: {
        setCount(count: number) {
            this.count = count;
        }
    },
    getters: {
        getCount: (state) => state.count,
    }
})
