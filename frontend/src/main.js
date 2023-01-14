import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App)

app.config.globalProperties.$baseUrl = import.meta.env.VITE_BASE_URL || "http://localhost:8080"
app.config.globalProperties.$apiUrl = import.meta.env.VITE_API_URL || "http://localhost:5000"

app.use(router)

app.mount('#app')
