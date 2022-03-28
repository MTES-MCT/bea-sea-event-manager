<template>
  <div id="app">
    <header-component></header-component>
    <router-view class="app-content"></router-view>
    <footer-component></footer-component>
  </div>
</template>

<script lang="ts" setup>
import HeaderComponent from "@/components/HeaderComponent.vue";
import FooterComponent from "@/components/FooterComponent.vue";
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  width: 100vw;
}

.app-content {
  width: 60vw;
  margin-right: auto;
  margin-left: auto;
}
</style>
