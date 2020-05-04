import Vue from 'vue'
import Vuex from 'vuex'
import axios from '../plugins/axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    system: null,
    ram: null,
    diskList: null,
    diskInfo: null
  },
  mutations: {
    system (state, data) {
      state.system = data
    },
    ram (state, data) {
      state.ram = data
    },
    diskList (state, data) {
      state.diskList = data
    },
    diskInfo (state, data) {
      state.diskInfo = data
    }
  },
  actions: {
    getInfoSystem ({ commit }) {
      axios
        .get(`/api/v1/info_system`)
        .then(Response => {
          commit('system', Response.data)
        })
        .catch(error => console.log(error))
    },
    getRamInfo ({ commit }) {
      axios
        .post(`/api/v1/memory_info`)
        .then(Response => {
          commit('ram', Response.data)
        })
        .catch(error => (console.log(error)))
    },
    getDiskList ({ commit }) {
      return new Promise((resolve, reject) => {
        axios.post('/api/v1/info_space_disk/', { timeout: 1500 })
          .then((response) => {
            commit('diskList', response.data)
            resolve(response.data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },
    getDiskInfo ({ commit }, path) {
      return new Promise((resolve, reject) => {
        axios.post('api/v1/info_space_disk/disk', {
          path: path
        }, { timeout: 1500 })
          .then((response) => {
            commit('diskInfo', response.data)
            resolve(response.data)
          })
          .catch((error) => {
            reject(error)
          })
      })
    },

    getCpuInfo ({ commit }) {
      axios.get(`/api/v1/cpu_info`)
        .then((response) => {
          commit('cpuInfo', response.data)
        })
        .catch((error) => console.log(error))
    }

  }
})
