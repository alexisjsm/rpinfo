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
        </v-container>
      </v-card>
    </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      cpu_info: 'null',
      infoName: ['Procesador', 'CPU Logico', 'CPU Fisico']

    }
  },
  methods: {
    get_cpuInfo () {
      axios
        .get('http://localhost:5000/api/v1/cpu_info')
        .then(Response => (this.cpu_info = Response.data))
        .catch(error => (console.log(error)))
    }
  },

  created () {
    this.get_cpuInfo()
  }
}
</script>
