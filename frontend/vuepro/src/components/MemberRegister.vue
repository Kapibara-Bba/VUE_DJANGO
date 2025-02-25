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
        <select v-model="selectedTeam" @change="updateTeam">
          <option value="">選択しない</option>
          <option v-for="team in formattedTeams" :key="team.id" :value="team.id">
            {{ team.label}}
          </option>
        </select>
      </div>
      <div>
        <label for="team-name">チーム名:</label>
        <input type="text" v-model="team_name" :disabled="selectedTeam !== ''" />
      </div>
      <div>
        <label for="director">チーム代表者:</label>
        <input type="text" v-model="director" :disabled="selectedTeam !== ''" />
      </div>
      <!-- 選択したユーザーのIDを hidden で保持 -->
      <input type="hidden" :value="selectedTeam" name="id" />
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
      teams: [],         // チームリスト
      selectedTeam: "", // 選択されたチームのID
    };
  },
  computed: {
    // フォーマット済みのユーザーリスト（「ユーザ名：太郎」の形式にする）
    formattedTeams() {
      return this.teams.map(team => ({
        id: team.id,
        label: `チーム名：${team.team_name} , 代表者：${team.director}` // 表示用のテキスト
      }));
    }
  },
  async mounted() {
    await this.fetchTeams();
  },
  methods: {
    async fetchTeams() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/register/", {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });
        const data = await response.json(); // メンバーリストを取得
        // チームリストをセット（フォーマット済み）
        this.teams = data.map(team => ({
          id: team.id,
          team_name: team.team_name,
          director: team.director,
          label: `チーム名：${team.team_name} , 代表者：${team.director}`
        }));
      } catch (error) {
        console.error("チーム情報の取得に失敗しました", error);
      }
    },
    updateTeam() {
      if (this.selectedTeam === "") {
        // 「選択しない」場合はテキストボックスを活性化し、空にする
        this.team_name = "";
        this.director = "";
      } else {
        // 選択したユーザーIDに対応するユーザー名を取得
        const team = this.teams.find(team => team.id === this.selectedTeam);
        this.team_name = team ? team.team_name : "";
        this.director = team ? team.director : "";
      }
    },
    async registerMember() {
      try {
        // const criteria = {
        //   name: this.name,
        //   password: this.password,
        //   team_name: this.team_name,
        //   director: this.director,
        //   team_id: this.selectedTeam
        // };

        let criteria = {};
        if (this.selectedTeam === "") {
          // 「選択しない」が選択された場合、新規ユーザー情報を送信
          criteria = {
            name: this.name,
            password: this.password,
            team_name: this.team_name,
            director: this.director,
          };
        } else {
          // 既存ユーザーを選択した場合、IDを送信
          criteria = { id: this.selectedTeam };
        }

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