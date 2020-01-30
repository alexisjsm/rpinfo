<template>
    <div class="system_info">
      <v-card>
        <v-container>
          <v-row align-content="center" justify="center">
            <v-col v-for="(info, key) in system_info" :key="key" cols="auto">
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
  name: 'SystemInfo',
  props: {
    host: String
  },
  data () {
    return {
      system_info: null,
      infoName: ['OS', 'Nombre del Sistema', 'version kernel', 'Distribución', 'Arch']
    }
  },

  methods: {
    get_infoSystem () {
      axios
        .get(`${this.host}/api/v1/info_system`)
        .then(Response => (this.system_info = Response.data))
        .catch(error => console.log(error))
    }
  },
  created () {
    this.get_infoSystem()
  }
}
</script>
<style lang="scss" scoped>

.c-title{
  font-size: 0.9rem
}
</style>
