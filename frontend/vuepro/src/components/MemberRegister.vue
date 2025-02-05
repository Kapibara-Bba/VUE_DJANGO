<template>
  <div>
    <h2>新規登録</h2>
    <form @submit.prevent="registerMember">
      <div>
        <label for="name">ユーザー名:</label>
        <input type="text" v-model="name" required />
      </div>
      <div>
        <label for="password">パスワード:</label>
        <input type="password" v-model="password" required />
      </div>
      <div>
        <label for="team">チーム選択:</label>
        <select v-model="selectedTeam">
          <option v-for="team in teams" :key="team.id" :value="team.id">
            {{ team.name}}
          </option>
        </select>
      </div>
      <div>
        <label for="team-name">チーム名:</label>
        <input type="text" v-model="team_name"/>
      </div>
      <div>
        <label for="director">チーム代表者:</label>
        <input type="text" v-model="director" />
      </div>
      <button type="submit">登録</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      name: "",
      password: "",
      team_name: "",
      director: "",
      team: [],         // チームリスト
      selectedTeam: null // 選択されたチームのID
    };
  },
  async created() {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/register/", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      // const response = await axios.get("http://127.0.0.1:8000/api/team/");
      this.members = response.data; // メンバーリストを取得
    } catch (error) {
      console.error("チーム情報の取得に失敗しました", error);
    }
  },
  methods: {
    async registerMember() {
      try {
        const criteria = {
          name: this.name,
          password: this.password,
          team_name: this.team_name,
          director: this.director,
          team_id: this.selectedTeam
        };

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
        console.error("登録エラー", error);
      }
    }
  }
};
</script>

<style scoped>
input, select {
  display: block;
  margin-bottom: 10px;
  padding: 8px;
  width: 100%;
}
button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
</style>