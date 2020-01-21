<template>
    <v-content>
        <v-container>
            <v-row>
                <v-col>
                    <system-info></system-info>
                </v-col>
            </v-row>
            <v-row>
                <v-col>
                    <info-disk></info-disk>
                </v-col>
            </v-row>
        </v-container>
    </v-content>

</template>

<script>
import SystemInfo from '../components/system_info.vue'
import InfoDisk from '../components/info_disk.vue'
export default {
  components: {
    SystemInfo,
    InfoDisk
  }
}
</script>
