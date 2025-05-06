<template>
  <form @submit.prevent="onSubmit">
    <div>
      <label for="username">ユーザ名</label>
      <input id="name" v-model="name" type="text" required />
    </div>
    <div>
      <label for="password">パスワード</label>
      <input id="password" v-model="password" type="password" required />
    </div>
    <button class="btn" type="submit">ログイン</button>
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

* {
  font-family:"Helvetica Neue", Helvetica, Arial;
}

form {
  background:#fff;
  border-radius:6px;
  padding:20px;
  padding-top:30px;
  width:430px;
  margin:5px auto;
  box-shadow:15px 15px 0px rgba(0,0,0,.1);
}

input {
  width:100%;
  background:#f5f5f5;
  border:0;
  padding:20px;
  border-radius:6px;
  margin-bottom:10px;
  border:1px solid #eee;
}

.btn {
  position:relative;
  width:100%;
  padding:20px;
  border-radius:6px;
  border:0;
  background:#f26964;
  font-size:1.2em;
  color:#fff;
  text-shadow:1px 1px 0px rgba(0,0,0,.1);
  box-shadow:0px 3px 0px #c1524e;
}

.btn:active {
  top:3px;
  box-shadow:none;
}

</style>
