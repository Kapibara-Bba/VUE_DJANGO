<template>
  <div>
    <h1>新規登録</h1>
    <form @submit.prevent="registerMember">
      <div>
        <label for="name">ユーザー名</label>
        <input type="text" v-model="name" required />
      </div>
      <div>
        <label for="password">パスワード</label>
        <input type="password" v-model="password" required />
      </div>
      <div>
        所属チーム
        <label class="select-team" for="team">
          <select v-model="selectedTeam" @change="updateTeam">
            <option value="">新規登録</option>
            <option v-for="team in formattedTeams" :key="team.id" :value="team.id">
              {{ team.label}}
            </option>
          </select>
        </label>
      </div>
      <div>
        <label for="team-name">チーム名</label>
        <input type="text" v-model="team_name" :disabled="selectedTeam !== ''" />
      </div>
      <div>
        <label for="director">チーム代表者</label>
        <input type="text" v-model="director" :disabled="selectedTeam !== ''" />
      </div>
      <!-- 選択したユーザーのIDを hidden で保持 -->
      <input type="hidden" :value="selectedTeam" name="id" />
      <button class="submit-btn" type="submit">登録</button>
      <button @click="goToLogin" type="button" class="btn btn-secondary">
        もどる
      </button>
    </form>
  </div>
</template>

<script>
import { useMemberStore } from "@/stores/memberStore";

export default {
  setup() {
    const store = useMemberStore();
    return { store };
  },

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
        // チームリストをセット
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
        // 選択したチームIDに対応するチーム名を取得
        const team = this.teams.find(team => team.id === this.selectedTeam);
        this.team_name = team ? team.team_name : "";
        this.director = team ? team.director : "";
      }
    },
    async registerMember() {
      try {
        let criteria = {};
        if (this.selectedTeam === "") {
          // 「選択しない」が選択された場合、新規ユーザー情報を送信
          criteria = {
            name: this.name,
            password: this.password,
            team_name: this.team_name,
            director: this.director,
            team_id: null,
          };
        } else {
          // 既存ユーザーを選択した場合、IDを送信
          criteria = {
            name: this.name,
            password: this.password,
            team_name: this.team_name,
            director: this.director,
            team_id: this.selectedTeam,
          };
        }

        const response = await fetch("http://127.0.0.1:8000/api/register/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(criteria),
        });
        if (response.status === 200){
          console.log('ログイン成功:');
          const data = await response.json();
          this.store.setData(data.user, data.team); // Pinia にユーザー情報を保存
          this.$router.push('/dashboard'); // トップ画面に遷移
        }
      } catch (error) {
        console.error("登録エラー", error);
      }
    },
    goToLogin() {
      this.$router.push('/'); // 新規登録画面に遷移
    }
  }
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
  padding-top: 20px;
}

form {
  background:#fff;
  border-radius:6px;
  padding:20px;
  padding-top:30px;
  width:430px ;
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

.submit-btn {
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

.btn {
  margin-top: 10px;
  width:100%;
  padding:20px;
  border-radius:6px;
  border:0;
  font-size:1.2em;
  color:#fff;
}

.submit-btn:active {
  top:3px;
  box-shadow:none;
}

.select-team {
    position: relative;
}

.select-team::before,
.select-team::after {
    position: absolute;
    content: '';
    pointer-events: none;
}

.select-team::before {
    right: 0;
    display: inline-block;
    width: 2.8em;
    height: 2.8em;
    border-radius: 0 3px 3px 0;
    background-color: #25d0b4;
    content: '';
}

.select-team::after {
    position: absolute;
    top: 50%;
    right: 1.4em;
    transform: translate(50%, -50%) rotate(45deg);
    width: 6px;
    height: 6px;
    border-bottom: 3px solid #fff;
    border-right: 3px solid #fff;
    content: '';
}

.select-team select {
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    min-width: 230px;
    height: 2.8em;
    padding: .4em 3.6em .4em .8em;
    border: 2px solid #25d0b4;
    border-radius: 3px;
    color: #333333;
    font-size: 1em;
    cursor: pointer;
}

.select-team select:focus {
    outline: 1px solid #25d0b4;
}

</style>