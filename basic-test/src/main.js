import Vue from 'vue'
import App from './App.vue'
import "@/assets/css/tailwind.css"
import router from '@/router'
import { VueSpinners } from '@saeris/vue-spinners'

Vue.use(VueSpinners)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
