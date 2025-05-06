<template>
  <div :class="layoutClass">
    <router-view />
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

const route = useRoute()

const layoutClass = computed(() => {
  return route.name === 'Login' || route.name === 'Register' ? 'login-background' : '' // ログイン画面と新規登録画面に背景色設定
})
</script>

<style>
.login-background {
  background-color: #63b47a;
  min-height: 100vh;
}
</style>