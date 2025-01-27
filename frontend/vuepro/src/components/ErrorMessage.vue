<template>
  <div class="error-message">
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  props: {
    message: {
      type: String,
      required: true,
    },
  },
};
</script>

<style scoped>
.error-message {
  color: red;
  margin-top: 1rem;
}
</style>
