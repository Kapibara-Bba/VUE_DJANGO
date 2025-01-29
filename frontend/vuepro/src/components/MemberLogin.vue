<template>
  <div class="login-container">
    <h1>ログイン</h1>
    <LoginForm @login="handleLogin" />
    <ErrorMessage v-if="errorMessage" :message="errorMessage" />
  </div>

  <!-- 新規登録ボタン -->
  <div>
    <p>アカウントをお持ちでない場合:</p>
    <button @click="goToRegister" class="register-button">
      新規登録
    </button>
  </div>
</template>

<script>
import LoginForm from "./LoginForm.vue";
import ErrorMessage from "./ErrorMessage.vue";

export default {
  components: {
    LoginForm,
    ErrorMessage,
  },
  data() {
    return {
      errorMessage: '',
    };
  },
  methods: {
    async handleLogin(criteria) {
      this.errorMessage = '';
      try {
        const response = await fetch("http://127.0.0.1:8000/api/login/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(criteria),
        });
        console.log('ログイン成功:', response.data);
        alert(response.data.message); // ログイン成功

        // const response = await this.$axios.post('http://127.0.0.1:8000/api/login/', criteria.password);
        // // ログイン成功時の処理
        // console.log('ログイン成功:', response.data);
        // alert(response.data.message); // ログイン成功
        // this.$router.push('/dashboard'); // ダッシュボード画面へ遷移
      } catch (error) {
        console.error('ログイン失敗:', error);
        this.errorMessage = 'ログインに失敗しました。ユーザー名またはパスワードを確認してください。';
      }
    },
    goToRegister() {
      this.$router.push('/register'); // 新規登録画面に遷移
    }
  },
};
</script>

<style>
/* 必要ならスタイルを追加 */
</style>
