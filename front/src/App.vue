<template>
<v-app >
  <v-container fluid>
    <v-row>
      <v-col>
        <view-menu> </view-menu>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <view-main></view-main>
      </v-col>
    </v-row>
  </v-container>
</v-app>
</template>

<script>
import ViewMenu from './layout/menu.vue'
import ViewMain from './layout/main.vue'
export default {

  components: {
    ViewMenu,
    ViewMain
  }
}
</script>
<style lang="scss" scoped>

</style>
