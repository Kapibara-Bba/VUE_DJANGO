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
    <div>
      <label for="member">メンバー選択:</label>
      <select v-model="selectedMember">
        <option v-for="member in members" :key="member.id" :value="member.id">
          {{ member.name }}
        </option>
      </select>
    </div>
    <button type="submit">登録</button>
  </form>
</template>

<script>
export default {
  name: "LoginForm",
  data() {
    return {
      name: '',
      password: '',
      team: '',
    };
  },
  methods: {
    onSubmit() {
      // 入力データを親に送信
      this.$emit('register', { name: this.name, password: this.password, team: this.team });
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
