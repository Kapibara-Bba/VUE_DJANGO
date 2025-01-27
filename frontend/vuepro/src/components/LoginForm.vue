<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="name">ユーザ名:</label>
      <input id="name" v-model="name" type="text" required />
    </div>
    <div>
      <label for="password">パスワード:</label>
      <input id="password" v-model="password" type="password" required />
    </div>
    <button type="submit">ログイン</button>
  </form>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      name: '',
      password: '',
    };
  },
  methods: {
    onSubmit() {
      // 入力データを親に送信
      this.$emit('login', { name: this.name, password: this.password });
    },
  },
};
</script>

<style scoped>
.form-group {
  margin-bottom: 1rem;
}
button {
  width: 100%;
  padding: 0.5rem;
}
</style>
