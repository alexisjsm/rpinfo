<template>
    <div class="cpu_info">
      <v-card>
        <v-container>
          <v-row align-content="center" justify="center">
            <v-col v-for="(info, key) in cpu_info" :key="key" cols="auto">
                <v-card-title class="text-center d-inline-flex">
                  <h3 class="title">{{infoName[key]}}</h3>
                </v-card-title>
                <v-card-text>
                    <p>{{info}}</p>
                </v-card-text>
            </v-col>
          </v-row>
          <v-row align-content="center" justify="center">
            <v-col cols="auto">
              <v-card-title>
                <h3 class="title"> CPU % </h3>
                </v-card-title>
                <v-card-text>
                  <p>{{cpu_percent[0]}}</p>
                </v-card-text>
              </v-col>
              <v-col v-for="(freq, name ) in cpu_frequent" :key="name" cols="auto">
                <v-card-title>
                <h3 class="title"> {{cpuFreqName[name]}}</h3>
                </v-card-title>
                <v-card-text>
                  <p>{{freq}}</p>
                </v-card-text>
              </v-col>
            </v-row>
        </v-container>
      </v-card>
    </div>
</template>
<script>
import axios from 'axios'
export default {

  props: {
    host: String
  },
  data () {
    return {
      cpu_info: null,
      infoName: ['Procesador', 'CPU Logico', 'CPU Fisico'],
      cpu_percent: '',
      cpu_frequent: '',
      cpuFreqName: ['Actual', 'Min', 'Max']

    }
  },
  methods: {
    get_cpuInfo () {
      axios
        .get(`${this.host}/api/v1/cpu_info`)
        .then(Response => (this.cpu_info = Response.data))
        .catch(error => (console.log(error)))
    },

    async get_cpuPercent () {
      const cpuPerc = axios
        .post(`${this.host}/api/v1/cpu_percent`, { timeout: 1 })
        .then(Response => (this.cpu_percent = Response.data))
        .catch(error => (console.log(error)))
      return cpuPerc
    },

    async get_cpuFrequent () {
      const cpuFreq = axios
        .post(`${this.host}/api/v1/cpu_frequent`, { timeout: 1 })
        .then(Response => (this.cpu_frequent = Response.data))
        .catch(error => (console.log(error)))
      return cpuFreq
    }
  },
  mounted () {
    this.get_cpuInfo()
    this.get_cpuPercent()
    this.get_cpuFrequent()
  }
}
</script>
