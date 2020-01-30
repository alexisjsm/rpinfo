<template>
<v-app >
  <v-content>
    <v-container>
      <v-row>
        <v-col>
          <view-menu></view-menu>
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          <view-main :host="host"></view-main>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</v-app>
</template>

<script>
import ViewMenu from './views/menu.vue'
import ViewMain from './views/main.vue'
export default {

  components: {
    ViewMenu,
    ViewMain
  },
  data () {
    return {
      host: `http://localhost:5000`
    }
  }
}
</script>
<style lang="scss" scoped>

</style>
