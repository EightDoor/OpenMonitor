import {createPinia} from 'pinia';
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate' //引入持久化插件

const store = createPinia();
store.use(piniaPluginPersistedstate)

export default store
