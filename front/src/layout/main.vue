<template>
    <v-content>
        <v-container>
            <v-row>
                <v-col cols="auto">
                    <system-info></system-info>
                </v-col>
            </v-row>
            <v-row>
                <v-col lg="4" cols="auto">
                    <info-disk></info-disk>
                </v-col>
            </v-row>
            <v-row>
                <v-col lg="4" cols="auto">
                    <cpu-info></cpu-info>
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
  }
}
</script>
