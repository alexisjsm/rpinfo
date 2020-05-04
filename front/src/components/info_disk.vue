<template>
    <div class = "info_disk">
      <v-card>
        <v-container>
      <v-card-title>
      <h1 class="title">HDD / SSD / USB</h1>
      </v-card-title>
          <v-row>
            <v-col align-self="center">
                  <v-select label="Selecciona disco"  v-model="selectedDisk"  :items="disklist" item-text="device" item-value="mountpoint">
                  </v-select>
              </v-col>
            <v-col align-self="center" cols="auto">
                <v-btn text icon color="green darken-1" :loading="loading" @click="refresh">
                  <v-icon>mdi-cached</v-icon>
                </v-btn>
              </v-col>
          </v-row>
          <v-row align-content="center" justify="center" >
              <v-col v-if="msgerror" cols="auto">
                <p>Disco no disponible </p>
              </v-col>
              <v-col v-for="(disco,key) in diskInfo" :key="key" cols="auto" v-else>
                  <v-card-title>
                     <h3 class="title d-inline-block"> {{infoDiskName[key]}} </h3>
                    </v-card-title>
                  <v-card-text>
                    <div v-if="disco.includes('%')" class="text-center">
                      <v-progress-circular :value="disco" color="green darken-1" size= "100" width="10">
                        {{disco}}
                      </v-progress-circular>
                    </div>
                    <div v-else>
                        <p> {{disco}} </p>
                      </div>
                  </v-card-text>
              </v-col>
          </v-row>
        </v-container>
      </v-card>
    </div>
</template>
<script>
export default {

  props: {
    host: String
  },
  data () {
    return {
      infoDiskName: ['Total', 'En uso', 'Libre', 'Porcentaje'],
      selectedDisk: '',
      msgerror: false,
      loading: false
    }
  },
  watch: {
    selectedDisk: {
      handler () {
        this.getdiskInfo()
      }
    },
    deep: true
  },
  computed: {
    disklist () {
      return this.$store.state.diskList
    },
    diskInfo () {
      return this.$store.state.diskInfo
    }
  },
  methods: {
    async getdiskInfo () {
      let diskInfo = await this.$store.dispatch('getDiskInfo', this.selectedDisk)
      console.log(diskInfo)
    },
    async getDistList () {
      let diskList = await this.$store.dispatch('getDiskList')
      console.log(diskList)
    },
    async refresh () {
      this.loading = true
      const refresh = Promise.all([this.getDistList(), this.getdiskInfo()])
        .then(() => (this.loading = false))
      return refresh
    }
  },
  mounted () {
    this.getDistList()
  }
}
</script>
<style lang="scss" scoped>

</style>
