// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import NProgress from 'nprogress'
import 'nprogress/nprogress.css'
import VueRouter from 'vue-router'
import Vuex from 'vuex'
import axios from 'axios'
import echarts from 'echarts'

Vue.prototype.$echarts = echarts

Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(VueRouter);
Vue.use(Vuex);


Vue.prototype.ajax = axios
axios.defaults.timeout = 5000
axios.defaults.baseUrl='http://127.0.0.1:8080'

axios.interceptors.request.use(config => {
    NProgress.start()
    return config
}, error => {
    return Promise.reject(error)
})
function checkStatus(response) {
  NProgress.done()
  if (response.status === 200 || response.status === 304) {
    return response
  }
  return {
    data: {
      code: -404,
      message: response.statusText,
      data: response.statusText
    }
  }
}
axios.interceptors.response.use(response => {
  checkStatus(response)
  return response
}, error => {
  return Promise.resolve(error.response)
})

router.beforeEach(function(to, from, next){
  NProgress.start()
  var usertoken = sessionStorage.getItem('usertoken')
  console.log(to.path+'  '+usertoken)
  if(!usertoken && to.path!='/'){
    NProgress.done()
    next({path:'/'})
  }else(
    next()
  )
});

router.afterEach(transition => {
  NProgress.done();
});


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
