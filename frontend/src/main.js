import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App)

app.config.globalProperties.$baseUrl = import.meta.env.VITE_BASE_URL || "http://127.0.0.1:8080"
app.config.globalProperties.$apiUrl = import.meta.env.VITE_API_URL || "http://127.0.0.1:5000"

app.use(router)

app.mount('#app')
