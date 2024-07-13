<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import LandingPage from './views/LandingPage.vue'
import Home from './views/Home.vue'
import DashBoard from './components/DashBoard.vue'
import Profile from './views/Profile.vue'
export default {
  name: 'App',
  components: {
    LandingPage,
    Home, DashBoard, Profile
  } 
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #6b0909;
  margin-top: 60px;
}
/* Add global styles here */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
</style>
