<template>
    <div class = "info_disk">
      <v-card>
        <v-container>
      <v-card-title>
      <h1 class="title">HDD / SSD / USB</h1>
      </v-card-title>
          <v-row>
            <v-col align-self="center">
                  <v-select label="Selecciona disco"  v-model="selectedDisk"  :items="disk_list" item-text="device" item-value="mountpoint">
                  </v-select>
              </v-col>
            <v-col align-self="center" cols="auto">
                <v-btn text icon color="red" :loading="loading" @click="refresh">
                  <v-icon>mdi-cached</v-icon>
                </v-btn>
              </v-col>
          </v-row>
          <v-row align-content="center" justify="center" >
              <v-col v-if="msgerror" cols="auto">
                <p>Disco no disponible </p>
              </v-col>
              <v-col v-for="(disco,key) in disk_info_space" :key="key" cols="auto" v-else>
                  <v-card-title>
                     <h3 class="title d-inline-block"> {{infoDiskName[key]}} </h3>
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

  props: {
    host: String
  },
  data () {
    return {
      disk_list: null,
      infoDiskName: ['Total', 'En uso', 'Libre', 'Porcentaje'],
      selectedDisk: '',
      disk_info_space: null,
      msgerror: false,
      loading: false
    }
  },
  watch: {
    selectedDisk: {
      handler () {
        this.get_DiskInfo()
      }
    },
    deep: true
  },
  methods: {
    async get_DiskList () {
      const disklist = await Axios
        .post(`${this.host}/api/v1/info_space_disk/`, { timeout: 1500 })
        .then(Response => (this.disk_list = Response.data))
        .catch(error => console.log(error))
      return disklist
    },
    async get_DiskInfo () {
      const disk = await Axios
        .post(`${this.host}/api/v1/info_space_disk/disk`,
          {
            path: this.selectedDisk
          }, { timeout: 1500 })
        .then(Response => {
          if (Response) {
            this.msgerror = false
            this.disk_info_space = Response.data
          }
        })
        .catch(error => {
          if (error) {
            this.msgerror = true
          }
        })
      return disk
    },
    async refresh () {
      this.loading = true
      const refresh = Promise.all([this.get_DiskList(), this.get_DiskInfo()])
        .then(() => (this.loading = false))
      return refresh
    }
  },
  mounted () {
    this.get_DiskList()
  }
}
</script>
<style lang="scss" scoped>

</style>
