<template>
    <div class = "info_disk">
      <v-card>
        <v-container>
          <v-row>
            <v-col>
                  <v-select label="Selecciona disco" name="disco" id="disco" v-model="selectedDisk"  :items="disk_list">
                  </v-select>
              </v-col>
          </v-row>

          <v-row>
              <v-col v-for="(disco,key) in disk_info_space" :key="key">
                  <v-card-title>{{key}}</v-card-title>
                  <card-text>
                      {{disco}}
                  </card-text>
              </v-col>
          </v-row>
        </v-container>
      </v-card>
    </div>
</template>
<script>
import Axios from 'axios'
export default {
  data () {
    return {
      disk_list: null,
      selectedDisk: '',
      disk_info_space: null
    }
  },
  watch: {
    selectedDisk (newDisk, oldDisk) {
      console.log(oldDisk)
      console.log(newDisk)
      this.get_SpaceDisk(newDisk)
    }
  },
  methods: {
    get_DiskList () {
      Axios
        .get('http://localhost:5000/api/v1/info_space_disk/')
        .then(Response => (this.disk_list = Response.data))
        .catch(error => console.log(error))
    },
    get_SpaceDisk (disk) {
      Axios
        .get('http://localhost:5000/api/v1/info_space_disk/' + disk)
        .then(Response => (this.disk_info_space = Response.data))
        .catch(error => console.log(error))
    }
  },

  created () {
    this.get_DiskList()
  }
}
</script>
<style lang="scss" scoped>

</style>
