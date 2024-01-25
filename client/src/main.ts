import './assets/main.css'

import { createApp } from 'vue'
import vue3GoogleLogin from 'vue3-google-login'
import App from './App.vue'

const app = createApp(App).use(vue3GoogleLogin, {
	clientId: import.meta.env.VITE_GOOGLE_API_KEY,
})

// app.use(router)

app.mount('#app')
