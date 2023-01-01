<template>
  <v-app>
    <v-main>
      <v-container fill-height fluid class="ma-0 pa-0 bg grey darken-4">
        <Nuxt></Nuxt>
      </v-container>
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'DefaultLayout',
  data() {
    return {
      title: 'Home',
    }
  },
})
</script>

<style href="./style.scss" />