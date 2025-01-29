<template>
  <div class="login-container">
    <h1>新規ユーザ登録</h1>
    <RegisterForm @register="handleRegister" />
  </div>
</template>

<script>
import RegisterForm from './RegisterForm.vue';

export default {
  components: {
    RegisterForm,
  },
  data() {
    return {
      errorMessage: '',
    };
  },
  methods: {
    async handleRegister(criteria) {
      this.errorMessage = '';
      try {
        const response = await fetch("http://127.0.0.1:8000/api/register/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(criteria),
        });
        console.log('ログイン成功:', response.data);
        alert(response.data.message); // ログイン成功
      } catch (error) {
        console.error('ログイン失敗:', error);
        this.errorMessage = 'ログインに失敗しました。ユーザー名またはパスワードを確認してください。';
      }
    },
  },
};
</script>