<template>
    <v-content>
            <v-row align-content="center" justify="space-around">
                <v-col lg=4 cols="auto">
                    <system-info :host="host"></system-info>
                </v-col>
                <v-col lg=8 cols="auto">
                    <cpu-info :host="host"></cpu-info>
                </v-col>
            </v-row>
            <v-row align-content="center" justify="space-around">
                <v-col lg=4 cols="auto">
                    <info-disk :host="host"></info-disk>
                </v-col>
                <v-col lg=8 cols="auto">
                    <info-ram :host="host"></info-ram>
                </v-col>
            </v-row>
    </v-content>

</template>

<script>
import SystemInfo from '../components/system_info.vue'
import InfoDisk from '../components/info_disk.vue'
import CpuInfo from '../components/info_cpu.vue'
import InfoRam from '../components/info_ram.vue'
export default {
  components: {
    SystemInfo,
    InfoDisk,
    CpuInfo,
    InfoRam
  },

  props: {
    host: String
  }
}
</script>
