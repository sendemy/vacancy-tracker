import './assets/main.css'

import { createApp } from 'vue'
import vue3GoogleLogin from 'vue3-google-login'
import App from './App.vue'

const app = createApp(App).use(vue3GoogleLogin, {
	clientId:
		'1022382885094-sr68t0rdkh78j1392lnd9gtogcnhr903.apps.googleusercontent.com',
})

// app.use(router)

app.mount('#app')
