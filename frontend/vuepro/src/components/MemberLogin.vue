<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username:</label>
        <input type="text" v-model="username" id="username" />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" v-model="password" id="password" />
      </div>
      <div>
        <label for="team">Team:</label>
        <input type="text" v-model="team" id="team" />
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      username: "",
      password: "",
      errorMessage: "",
    };
  },
  methods: {
    async login() {
      try {
        console.log("Sending request to Django...");
        const response = await axios.post("http://127.0.0.1:8000/api/login/", {
          team: this.team,
          name: this.username,
          
        });
        console.log("Response from Django:", response.data);
        alert(response.data.message); // ログイン成功
      } catch (error) {
        console.error("Error:", error);
        // エラーオブジェクトを確認し、エラーメッセージを安全に取得
        if (error.response) {
          this.errorMessage =
            error.response.data.error || "An error occurred during login.";
        } else {
          this.errorMessage = "Network error or server is unreachable.";
        }
      }
    },
  },
};
</script>

<style>
/* 必要ならスタイルを追加 */
</style>
