<script setup>
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
</script>

<template>
  <header>
    <NavBar></NavBar>
  </header>
  
  <RouterView />
</template>
