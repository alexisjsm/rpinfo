<template>
    <div class="system_info">
      <v-card with="400">
        <v-cointaner>
          <v-row>
            <v-col v-for="(info, key) in system_info" :key="key">
                <v-card-title>{{key}}</v-card-title>
                <v-card-text>
                    {{info}}
                </v-card-text>
          </v-col>
        </v-row>
        </v-cointaner>
      </v-card>
    </div>
</template>
<script>
import axios from 'axios'

export default {
  data () {
    return {
      system_info: null
    }
  },

  methods: {
    get_infoSystem () {
      axios
        .get('http://localhost:5000/api/v1/info_system')
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

</style>
