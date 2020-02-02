<template>
    <div class="cpu_info">
      <v-card>
        <v-container>
      <v-card-title>
        <h1 class="title">CPU</h1>
      </v-card-title>
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
          <v-row>
            <v-col align-self="center">
              <v-sparkline
              :fill="false"
              :value="cpuTemp"
              :gradient="colors"
              :smooth="true"
              line-width="2"
              :radius="10"
              :show-labels="true"
              :auto-line-width="false"
              >
              </v-sparkline>
            </v-col>
          </v-row>
          <v-row align-content="center" justify="center">
              <v-col v-for="(freq, name ) in cpu_frequent" :key="name" cols="auto">
                <v-card-title>
                <h3 class="title"> {{cpuFreqName[name]}}</h3>
                </v-card-title>
                <v-card-text>
                  <p>{{freq}}</p>
                </v-card-text>
              </v-col>
            <v-col cols="auto">
              <v-card-title>
                <h3 class="title">Porcentaje</h3>
              </v-card-title>
              <v-card-text>
                <div class="text-center">
                    <v-progress-circular :value="cpu_percent[0]" color="blue darken-1" size= "100" width="10">
                        {{cpu_percent[0]}}%
                    </v-progress-circular>
                </div>
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
      cpuFreqName: ['Actual', 'Min', 'Max'],
      colors: ['#E53935', '#FB8C00', '#FFB300', '#FDD835', '#C0CA33', '#00ACC1', '#039BE5'],
      cpuTemp: []
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
      const cpuPerc = setInterval(() => {
        axios
          .post(`${this.host}/api/v1/cpu_percent`)
          .then(Response => (this.cpu_percent = Response.data))
          .catch(error => (console.log(error)))
      }, 1000)
      return cpuPerc
    },

    async get_cpuFrequent () {
      const cpuFreq = axios
        .post(`${this.host}/api/v1/cpu_frequent`)
        .then(Response => (this.cpu_frequent = Response.data))
        .catch(error => (console.log(error)))
      return cpuFreq
    },

    async get_cpuTemp () {
      const cpuTemp = setInterval(() => {
        axios.get(`${this.host}/api/v1/cpu_temp`)
          .then(Response => {
            this.cpuTemp.push(Response.data)
            if (this.cpuTemp.length >= 15) {
              this.cpuTemp.shift()
            }
          })
          .catch(error => (console.log(error)))
      }, 2000)
      return cpuTemp
    }

  },
  mounted () {
    this.get_cpuPercent()
    this.get_cpuInfo()
    this.get_cpuFrequent()
    this.get_cpuTemp()
  }
}
</script>
