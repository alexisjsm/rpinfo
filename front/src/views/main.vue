<template>
    <v-content>
        <v-container>
            <v-row>
                <v-col >
                    <system-info :host="this.host"></system-info>
                </v-col>
            </v-row>
            <v-row>
                <v-col lg="4">
                    <info-disk :host="this.host"></info-disk>
                </v-col>
                <v-col>
                    <cpu-info :host="this.host"></cpu-info>
                </v-col>
            </v-row>

        </v-container>
    </v-content>

</template>

<script>
import SystemInfo from '../components/system_info.vue'
import InfoDisk from '../components/info_disk.vue'
import CpuInfo from '../components/info_cpu.vue'
export default {
  components: {
    SystemInfo,
    InfoDisk,
    CpuInfo
  },

  props: {
    host: String
  }
}
</script>
