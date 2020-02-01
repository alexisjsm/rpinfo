<template>
    <div id="info_ram">
        <v-card>
            <v-container>
              <v-card-title>
                <h1 class="title"> Memoria RAM</h1>
              </v-card-title>
                <v-row align-content="center" justify="center">
                    <v-col v-for="(r,key) in ram" :key="key" cols="auto">
                      <v-card-title>
                            <h3 class="title">{{ramName[key]}}</h3>
                      </v-card-title>
                  <v-card-text>
                      <div v-if="r.includes('%')" class="text-center">
                        <v-progress-circular :value="r" color="yellow darken-1" size= "100" width="10">
                          {{r}}
                        </v-progress-circular>
                      </div>
                      <div v-else>
                          <p> {{r}} </p>
                        </div>
                  </v-card-text>
                    </v-col>
                </v-row>
            </v-container>
        </v-card>
    </div>
</template>
<script>
import Axios from 'axios'
export default {

  props: {
    host: String
  },
  data () {
    return {
      ram: null,
      ramName: ['Total', 'Disponible', 'Porcentaje', 'En uso', 'Libre']
    }
  },
  methods: {
    async get_ram_info () {
      const ram = setInterval(() => {
        Axios
          .get(`${this.host}/api/v1/memory_info`)
          .then(Response => (this.ram = Response.data))
          .catch(error => (console.log(error)))
      }, 1000)
      return ram
    }
  },

  mounted () {
    this.get_ram_info()
  }
}
</script>
