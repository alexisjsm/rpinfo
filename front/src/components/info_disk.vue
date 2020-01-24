<template>
    <div class = "info_disk">
      <v-card>
        <v-container>
          <v-row  align-content="center" justify="center">
            <v-col>
                  <v-select label="Selecciona disco" v-model="selectedDisk"  :items="disk_list" item-text="device" item-value="mountpoint">
                  </v-select>
              </v-col>
          </v-row>

          <v-row align-content="center" justify="center">
              <v-col v-for="(disco,key) in disk_info_space" :key="key" cols="auto">
                  <v-card-title>
                     <h3 class="title d-inline-block"> {{key}} </h3>
                    </v-card-title>
                  <v-card-text>
                     <p> {{disco}} </p>
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
  name: 'InfoDisk',

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
      this.get_DiskInfo()
    }
  },
  methods: {
    async get_DiskList () {
      const disklist = await Axios
        .get('http://localhost:5000/api/v1/info_space_disk/')
        .then(Response => (this.disk_list = Response.data))
        .catch(error => console.log(error))
      return disklist
    },
    async get_DiskInfo () {
      const disk = await Axios
        .post('http://localhost:5000/api/v1/info_space_disk/disk', {
          path: this.selectedDisk
        })
        .then(Response => (this.disk_info_space = Response.data))
        .catch(error => console.log(error))
      return disk
    }
  },

  updated () {
    this.get_DiskList()
  }
}
</script>
<style lang="scss" scoped>

</style>
