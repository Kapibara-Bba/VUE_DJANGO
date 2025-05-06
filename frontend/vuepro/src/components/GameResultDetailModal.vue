<template>
  <div class="modal-background">
    <div class="modal-content">
      <h2 class="modal-title">試合結果詳細</h2>
      <form @submit.prevent="updateGameResult">
        <div class="modal-body">
          <div class="input-content">
            <label class="form-label">試合日時</label>
            <input v-model="editedGameResult.game_date" type="date" required />
            <p v-if="errors.game_date" class="text-danger">{{ errors.game_date }}</p>
          </div>
          <div class="input-content">
            <label class="form-label">対戦相手</label>
            <input v-model="editedGameResult.opponent" required />
            <p v-if="errors.opponent" class="text-danger">{{ errors.opponent }}</p>
          </div>
          <div class="input-content">
            <label class="form-label">得点</label>
            <input v-model="editedGameResult.my_team_score" @input="validateScore('my_team')" required />
            <p v-if="errors.my_team_score" class="text-danger">{{ errors.my_team_score }}</p>
          </div>
          <div class="input-content">
            <label class="form-label">失点</label>
            <input v-model="editedGameResult.opponent_score" @input="validateScore('opponent')" required />
            <p v-if="errors.opponent_score" class="text-danger">{{ errors.opponent_score }}</p>
          </div>
          <div class="input-content">
            <label class="form-label">勝ち投手</label>
            <input v-model="editedGameResult.winning_pitcher" />
          </div>
          <div class="input-content">
            <label class="form-label">負け投手</label>
            <input v-model="editedGameResult.losing_pitcher" />
          </div>
          <div class="input-content">
            <label class="form-label">セーブ投手</label>
            <input v-model="editedGameResult.save_pitcher" />
          </div>
          <div class="input-content">
            <label class="form-label">本塁打</label>
            <input v-model="editedGameResult.home_run" />
          </div>
          <div class="input-content">
            <label class="form-label">備考</label>
            <textarea v-model="editedGameResult.notes"></textarea>
          </div>
        </div>
        <div class="modal-buttons">
          <button type="submit" class="update-btn">更新</button>
          <button type="button" class="delete-btn" @click="deleteGameResult">削除</button>
          <button type="button" class="close-btn" @click="$emit('close')">閉じる</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  emits: ['update-game-result'],
  data() {
    return {
      editedGameResult: { ...this.gameResult },
      errors: {
        game_date: '',
        opponent: '',
        my_team_score: '',
        opponent_score: ''
      }
    };
  },
  methods: {
    validateDate() {
      // 試合日のバリデーションチェック
      const value = this.editedGameResult.game_date;

      if (value === '' || value === null) {
        this.errors[`game_date`] = '試合日を入力してください。';
      } else {
        this.errors[`game_date`] = '';
      }
    },
    validateOpponent() {
      // 対戦相手のバリデーションチェック
      const value = this.editedGameResult.opponent;

      if (value === '' || value === null) {
        this.errors[`opponent`] = '対戦相手を入力してください。';
      } else {
        this.errors[`opponent`] = '';
      }
    },
    validateScore(team) {
      // 得点・失点のバリデーションチェック
      const value = team === 'my_team' ? this.editedGameResult.my_team_score : this.editedGameResult.opponent_score;

      if (value === '' || value === null) {
        this.errors[`${team}_score`] = '得点/失点を入力してください。';
      } else if (!Number.isInteger(Number(value)) || value < 0) {
        this.errors[`${team}_score`] = '得点と失点は0以上の整数で入力してください。';
      } else {
        this.errors[`${team}_score`] = '';
      }
    },
    updateGameResult() {
      // バリデーションチェック
      this.validateDate();
      this.validateOpponent();
      this.validateScore('my_team');
      this.validateScore('opponent');

      // エラーがある場合は送信中止
      if (this.errors.game_date || this.errors.opponent || this.errors.my_team_score || this.errors.opponent_score) {
        return;
      }

      // 親コンポーネントに入力情報を渡す
      this.$emit('update-game-result', {
        game_result_id: this.editedGameResult.game_result_id,
        game_date: this.editedGameResult.game_date,
        opponent: this.editedGameResult.opponent,
        my_team_score: this.editedGameResult.my_team_score,
        opponent_score: this.editedGameResult.opponent_score,
        winning_pitcher: this.editedGameResult.winning_pitcher,
        losing_pitcher: this.editedGameResult.losing_pitcher,
        save_pitcher: this.editedGameResult.save_pitcher,
        home_run: this.editedGameResult.home_run,
        notes: this.editedGameResult.notes,
      });
    },
    deleteGameResult() {
      this.$emit('delete-game-result', this.editedGameResult.game_result_id);
    }
  },
  props: ['gameResult'],
};
</script>

<style scoped>
.modal-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  width: 95%;
  max-width: 900px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
  height: 95%;
}

.modal-body {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 2列で並べる */
  gap: 5px;
  overflow-y: auto;
}

.modal-content h2 {
  color: #063970;
  margin-bottom: 1rem;
}

input, textarea {
  width: 100%;
  margin: 0.25rem 0;
  padding: 0.8rem;
  border: 2px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
}

textarea {
  resize: vertical;
}

.modal-buttons {
  display: flex;
  justify-content: right;
  margin-top: 5px;
}

.update-btn {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 10px;
  cursor: pointer;
}

.delete-btn {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 10px;
  cursor: pointer;
  margin-left: 25px;
}

.close-btn {
  background-color: #63b47a;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 10px;
  cursor: pointer;
  margin-left: 25px;
}

.form-label{
  margin-bottom: 0;
}

.input-content{
  margin-bottom: 0;
}
</style>
