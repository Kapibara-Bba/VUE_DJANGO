<template>
  <div>
    <header>
      <div class="team-name" v-if="teamData">⚾ {{ teamData.team_name }}</div>
      <div class="user-name" v-if="member">ログインユーザー：{{ member.name }}</div>
      <div>
        <!-- ログアウトボタン -->
        <button @click="logout" class="btn btn-danger">ログアウト</button>
      </div>
    </header>

    <div class="container-fluid main-container">
      <div class="row g-4">
        <!-- メンバー一覧 -->
        <div class="col-md-3">
          <div class="card">
            <div class="card-header">メンバー一覧</div>
            <ul class="list-group list-group-flush" v-for="member in teamData.members" :key="member">
              <li class="list-group-item">{{ member.name }}</li>
            </ul>
          </div>
        </div>

        <!-- 試合結果 -->
        <div class="col-md-6">
          <div class="card">
            <div class="card-header">試合結果一覧</div>
            <table class="table table-striped">
              <thead>
                <tr>
                  <th>試合日</th>
                  <th>対戦相手</th>
                  <th>スコア</th>
                  <th>勝敗</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="game in teamData.gameresults" :key="game.id" @click="openGameResultDetailModal(game)" style="cursor: pointer;">
                  <td>{{ game.game_date }}</td>
                  <td>{{ game.opponent }}</td>
                  <td>{{ game.my_team_score }} - {{ game.opponent_score }}</td>
                  <td :class="getResultStatus(game.my_team_score, game.opponent_score)">
                    {{ getResultStatusText(game.my_team_score, game.opponent_score) }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <button class="insert-button" @click="createGameResultModal = true">
            🗓️ 試合結果を追加する
          </button>
          <GameResultModal v-if="createGameResultModal" @close="createGameResultModal = false" @save="handleGameResultSave" />
          <GameResultDetailModal v-if="isGameResultDetailModalOpen" :gameResult="selectedGameResult" @close="isGameResultDetailModalOpen = false" @update-game-result="handleGameResultUpdate" @delete-game-result="handleGameResultDelete" />
        </div>

        <!-- 今後のスケジュール -->
        <div class="col-md-3">
          <div class="card">
            <div class="card-header">今後のスケジュール</div>
            <ul class="list-group list-group-flush">
              <li class="list-group-item" v-for="schedule in teamData.schedules" :key="schedule.id" @click="openScheduleDetail(schedule)" style="cursor: pointer;">
                {{ schedule.plan_date }}：{{ schedule.schedule_name }}
              </li>
            </ul>
          </div>
          <button class="insert-button" @click="createScheduleModal = true">
            🗓️ 予定を追加する
          </button>
          <ScheduleModal v-if="createScheduleModal" @close="createScheduleModal = false" @save="handleScheduleSave" />
          <ScheduleDetailModal v-if="isScheduleDetailModalOpen" :schedule="selectedSchedule" @close="isScheduleDetailModalOpen = false" @update-schedule="handleScheduleUpdate" @delete-schedule="handleScheduleDelete" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useMemberStore } from "@/stores/memberStore";
import { computed } from "vue";
import ScheduleModal from './ScheduleModal.vue'
import ScheduleDetailModal from "./ScheduleDetailModal.vue";
import GameResultModal from "./GameResultModal.vue";
import GameResultDetailModal from "./GameResultDetailModal.vue";

export default {
  components: {
    ScheduleModal,
    ScheduleDetailModal,
    GameResultModal,
    GameResultDetailModal
  },
  data() {
    return {
      createScheduleModal: false, // スケジュール登録用モーダル
      isScheduleDetailModalOpen: false, // スケジュール詳細モーダル
      selectedSchedule: null, // 選択スケジュール
      createGameResultModal: false, // 試合結果登録モーダル
      isGameResultDetailModalOpen: false, // 試合結果詳細モーダル
      selectedGameResult: null, // 選択試合結果
    }
  },
  setup() {
    // 画面遷移時にユーザとチーム情報を取得
    const store = useMemberStore();

    console.log("teamInfo")
    console.log(store.getTeamData);
    return {
      member: computed(() => store.getMember),
      teamData: computed(() => store.getTeamData),
    };
  },
  methods: {
    async handleScheduleSave(data) {
      // スケジュール登録処理
      try {
        const teamId = this.member.team_id;
        const response = await fetch(`http://127.0.0.1:8000/api/${teamId}/schedules/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });
        if (response.status === 200){
          console.log('スケジュール登録成功:');

          await this.fetchScheduleList(); // スケジュール一覧を再取得

          this.createScheduleModal = false; // モーダル閉じる
        }
      } catch (error) {
        console.error('スケジュール登録失敗:', error);
      }
    },
    async fetchScheduleList() {
      // スケジュール一覧取得
      try {
        const teamId = this.member.team_id;
        const response = await fetch(`http://127.0.0.1:8000/api/${teamId}/schedules/`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        });

        const data = await response.json();
        console.log('取得したスケジュールリスト:', data);

        this.teamData.schedules = data; // スケジュール一覧にセット

      } catch (error) {
        console.error('スケジュール取得失敗:', error);
      }
    },
    async handleScheduleUpdate(updatedSchedule) {
      // スケジュール更新
      try {
        const teamId = this.member.team_id;
        const response = await fetch(`http://127.0.0.1:8000/api/${teamId}/schedules/${updatedSchedule.schedule_id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(updatedSchedule),
        });

        if (!response.ok) {
          throw new Error('更新に失敗しました');
        }

        await this.fetchScheduleList(); // スケジュール一覧を再取得
        this.isScheduleDetailModalOpen = false;
      } catch (error) {
        console.error('スケジュール更新エラー:', error);
      }
    },
    async handleScheduleDelete(scheduleId) {
      // スケジュール削除
      try {
        const teamId = this.member.team_id;
        const response = await fetch(`http://127.0.0.1:8000/api/${teamId}/schedules/${scheduleId}/`, {
          method: 'DELETE',
        });

        if (!response.ok) {
          throw new Error('削除に失敗しました');
        }

        await this.fetchScheduleList(); // スケジュール一覧を再取得
        this.isScheduleDetailModalOpen = false;
      } catch (error) {
        console.error('スケジュール削除エラー:', error);
      }
    },
    openScheduleDetail(schedule) {
      // スケジュール詳細モーダルウィンドウ
      this.selectedSchedule = schedule;
      this.isScheduleDetailModalOpen = true;  // モーダル開く
    },
    async fetchGameResults() {
      // 試合結果一覧取得
      try {
        const teamId = this.member.team_id;
        const response = await fetch(`http://127.0.0.1:8000/api/${teamId}/game-result/`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        });

        if (!response.ok) throw new Error('試合結果取得失敗');
        this.teamData.gameresults = await response.json();
      } catch (error) {
        console.error('試合結果取得エラー:', error);
      }
    },
    async handleGameResultSave(data) {
      // 試合結果登録処理
      try {
        const teamId = this.member.team_id;
        const response = await fetch(`http://127.0.0.1:8000/api/${teamId}/game-result/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });
        if (response.status === 200){
          console.log('試合結果登録成功:');

          await this.fetchGameResults(); // 試合結果一覧を再取得
          this.createGameResultModal = false; // モーダル閉じる
        }
      } catch (error) {
        console.error('試合結果登録失敗:', error);
      }
    },
    async handleGameResultUpdate(updatedGameResult) {
      // 試合結果更新
      try {
        const teamId = this.member.team_id;
        const response = await fetch(`http://127.0.0.1:8000/api/${teamId}/game-result/${updatedGameResult.game_result_id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(updatedGameResult),
        });

        if (!response.ok) {
          throw new Error('更新に失敗しました');
        }

        await this.fetchGameResults(); // 試合結果一覧を再取得
        this.isGameResultDetailModalOpen = false; // モーダル閉じる
      } catch (error) {
        console.error('試合結果更新エラー:', error);
      }
    },
    async handleGameResultDelete(gameResultId) {
      // 試合結果削除
      try {
        const teamId = this.member.team_id;
        const response = await fetch(`http://127.0.0.1:8000/api/${teamId}/game-result/${gameResultId}/`, {
          method: 'DELETE',
        });

        if (!response.ok) {
          throw new Error('削除に失敗しました');
        }

        await this.fetchGameResults(); // 試合結果一覧を再取得
        this.isGameResultDetailModalOpen = false; // モーダル閉じる
      } catch (error) {
        console.error('試合結果削除エラー:', error);
      }
    },
    openGameResultDetailModal(game) {
      // 試合結果詳細モーダルウィンドウ
      this.selectedGameResult = game;
      this.isGameResultDetailModalOpen = true;  // モーダル開く
    },
    getResultStatus(ownScore, opponentScore) {
      // 勝敗の色分け用クラス定義
    if (ownScore > opponentScore) {
      return "win";
    } else if (ownScore < opponentScore) {
      return "lose";
    } else {
      return "draw";
    }
    },
    getResultStatusText(ownScore, opponentScore) {
      // 勝敗の文字分け
      if (ownScore > opponentScore) {
        return "勝";
      } else if (ownScore < opponentScore) {
        return "敗";
      } else {
        return "引分";
      }
    },
    logout() {
      // ログイン画面に遷移
      this.$router.push('/');
    }
  }
};

</script>

<style scoped>
header {
  background-color: #003366;
  color: white;
  position: relative;
  height: 70px;
  display: flex;
  align-items: center;
  padding: 0 30px;
}

.team-name {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
  font-size: 24px;
  font-weight: bold;
}

.user-name {
  margin-left: auto;
  font-size: 16px;
}

.main-container {
  padding: 30px;
}

.card {
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  border-left: 5px solid #dc3545;
}

.card-header {
  background-color: #002f6c;
  color: white;
  font-size: 20px;
}

ul.list-group li {
  font-size: 16px;
}

.insert-button {
  background-color: #063970;
  color: #fff;
  border: none;
  padding: 1rem 2rem;
  font-size: 1.2rem;
  border-radius: 30px;
  cursor: pointer;
  transition: 0.3s;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
}

.insert-button:hover {
  background-color: #0b5595;
}

.win {
  color: #4682b4;
  font-weight: bold;
}

.lose {
  color: #b22222;
  font-weight: bold;
}

.draw {
  color: #2e8b57;
  font-weight: bold;
}

</style>