<template>
    <v-content>
        <v-container>
            <v-row align-content="center" justify="center">
                <v-col>
                    <system-info :host="host"></system-info>
                </v-col>
            </v-row>
            <v-row>
                <v-col lg=4>
                    <info-disk :host="host"></info-disk>
                </v-col>
                <v-col>
                    <cpu-info :host="host"></cpu-info>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <info-ram :host="host"></info-ram>
                </v-col>
            </v-row>

        </v-container>
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
