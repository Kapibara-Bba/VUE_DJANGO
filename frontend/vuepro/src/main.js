import { createApp } from 'vue';
import { createPinia } from 'pinia'
import App from './App.vue';
import router from './index.js';
import axios from 'axios';

const pinia = createPinia()
const app = createApp(App).use(pinia).mount('#app');

app.use(router); // ルーターを使用
// Axiosをグローバルに登録
app.config.globalProperties.$axios = axios;

app.mount('#app');
