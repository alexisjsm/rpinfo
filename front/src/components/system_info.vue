<template>
    <div class="systemInfo">
      <v-card>
        <v-container>
          <v-card-title>
            <h1 class="title">General</h1>
          </v-card-title>
          <v-row align-content="center" justify="center">
            <v-col v-for="(info, key) in systemInfo" :key="key" cols="auto">
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

export default {
  name: 'SystemInfo',
  props: {
    host: String
  },
  data () {
    return {
      infoName: ['OS', 'Nombre del Sistema', 'version kernel', 'Distribución', 'Arch']
    }
  },
  computed: {
    systemInfo () {
      return this.$store.state.system
    }
  },
  methods: {
    getInfoSystem () {
      this.$store.dispatch('getInfoSystem')
    }
  },
  created () {
    this.getInfoSystem()
  }
}
</script>
<style lang="scss" scoped>

.c-title{
  font-size: 0.9rem
}
</style>
