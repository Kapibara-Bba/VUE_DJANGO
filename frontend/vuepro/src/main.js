import { createApp } from 'vue';
import App from './App.vue';
import router from './index.js';
import axios from 'axios';

const app = createApp(App);

app.use(router); // ルーターを使用
// Axiosをグローバルに登録
app.config.globalProperties.$axios = axios;

app.mount('#app');
