<template>
  <div class="login-container">
    <h1>ログイン</h1>
    <LoginForm @login="handleLogin" />
    <ErrorMessage v-if="errorMessage" :message="errorMessage" />
  </div>

  <!-- 新規登録ボタン -->
  <div class="register-btn">
    <h1>アカウントをお持ちでない場合</h1>
    <button @click="goToRegister" type="button" class="btn">
      新規登録
    </button>
  </div>
</template>

<script>
import LoginForm from "./LoginForm.vue";
import ErrorMessage from "./ErrorMessage.vue";
import { useMemberStore } from "@/stores/memberStore";
// import onMounted from "vue";

export default {
  components: {
    LoginForm,
    ErrorMessage,
  },
  setup() {
    const store = useMemberStore();
    return { store };
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
        if (response.status === 200){
          console.log('ログイン成功:');
          // alert(response.data); // ログイン成功
          const data = await response.json();
          this.store.setData(data.user, data.team); // Pinia にユーザーとチーム情報を保存
          this.$router.push('/dashboard'); // ダッシュボード画面に遷移
        }
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

<style scoped>
* {
  font-family:"Helvetica Neue", Helvetica, Arial;
}

h1 {
  text-align:center;
  font-size:1.4em;
  font-weight:700;
  color:white;
  padding-top: 60px;
}

.register-btn {
  text-align: center;
  margin-top: 50px;
  color: white;
}

.btn {
  position:relative;
  width:350px;
  padding:20px;
  border-radius:6px;
  border:0;
  background:#f26964;
  font-size:1.2em;
  color:#fff;
  text-shadow:1px 1px 0px rgba(0,0,0,.1);
  box-shadow:0px 3px 0px #c1524e;
}
</style>
