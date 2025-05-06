<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>📝 試合結果の追加</h2>
      <div class="modal-body">
        <div class="input-content">
          <label class="form-label">試合日時</label>
          <input v-model="game_date" type="date" placeholder="試合日" />
          <p v-if="errors.game_date" class="text-danger">{{ errors.game_date }}</p>
        </div>
        <div class="input-content">
          <label class="form-label">対戦相手</label>
          <input v-model="opponent" placeholder="対戦相手" />
          <p v-if="errors.opponent" class="text-danger">{{ errors.opponent }}</p>
        </div>
        <div class="input-content">
          <label class="form-label">得点</label>
          <input v-model="my_team_score" @input="validateScore('my_team')" placeholder="得点" />
          <p v-if="errors.my_team_score" class="text-danger">{{ errors.my_team_score }}</p>
        </div>
        <div class="input-content">
          <label class="form-label">失点</label>
          <input v-model="opponent_score" @input="validateScore('opponent')" placeholder="失点" />
          <p v-if="errors.opponent_score" class="text-danger">{{ errors.opponent_score }}</p>
        </div>
        <div class="input-content">
          <label class="form-label">勝ち投手</label>
          <input v-model="winning_pitcher" placeholder="勝ち投手" />
        </div>
        <div class="input-content">
          <label class="form-label">負け投手</label>
          <input v-model="losing_pitcher" placeholder="負け投手" />
        </div>
        <div class="input-content">
          <label class="form-label">セーブ投手</label>
          <input v-model="save_pitcher" placeholder="セーブ投手" />
        </div>
        <div class="input-content">
          <label class="form-label">本塁打</label>
          <input v-model="home_run" placeholder="本塁打" />
        </div>
        <div class="input-content">
          <label class="form-label">備考</label>
          <textarea v-model="notes" placeholder="備考"></textarea>
        </div>
      </div>
      <div class="buttons">
        <button class="save" @click="submit">⚾ 登録</button>
        <button class="cancel" @click="$emit('close')">キャンセル</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      game_date: '',
      opponent: '',
      my_team_score: '',
      opponent_score: '',
      winning_pitcher: '',
      losing_pitcher: '',
      save_pitcher: '',
      home_run: '',
      notes: '',
      errors: {
        game_date: '',
        opponent: '',
        my_team_score: '',
        opponent_score: ''
      }
    }
  },
  methods: {
    validateDate() {
      // 試合日のバリデーションチェック
      const value = this.game_date;

      if (value === '' || value === null) {
        this.errors[`game_date`] = '試合日を入力してください。';
      } else {
        this.errors[`game_date`] = '';
      }
    },
    validateOpponent() {
      // 対戦相手のバリデーションチェック
      const value = this.opponent;

      if (value === '' || value === null) {
        this.errors[`opponent`] = '対戦相手を入力してください。';
      } else {
        this.errors[`opponent`] = '';
      }
    },
    validateScore(team) {
      // 得点・失点のバリデーションチェック
      const value = team === 'my_team' ? this.my_team_score : this.opponent_score;

      if (value === '' || value === null) {
        this.errors[`${team}_score`] = '得点/失点を入力してください。';
      } else if (!Number.isInteger(Number(value)) || value < 0) {
        this.errors[`${team}_score`] = '得点と失点は0以上の整数で入力してください。';
      } else {
        this.errors[`${team}_score`] = '';
      }
    },
    submit() {
      // バリデーションチェック
      this.validateDate();
      this.validateOpponent();
      this.validateScore('my_team');
      this.validateScore('opponent');

      // エラーがある場合は送信中止
      if (this.errors.game_date || this.errors.opponent || this.errors.my_team_score || this.errors.opponent_score) {
        return;
      }

      // 入力値を親コンポーネントに送る
      const gameResultData = {
        game_date: this.game_date,
        opponent: this.opponent,
        my_team_score: this.my_team_score,
        opponent_score: this.opponent_score,
        winning_pitcher: this.winning_pitcher,
        losing_pitcher: this.losing_pitcher,
        save_pitcher: this.save_pitcher,
        home_run: this.home_run,
        notes: this.notes,
      };
      this.$emit('save', gameResultData);
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 20px;
  width: 95%;           /* 横幅広くする */
  max-width: 900px;      /* 900pxくらいまで拡張 */
  border-radius: 8px;
  overflow: hidden;
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

.buttons {
  margin-top: 0.5rem;
  display: flex;
  justify-content: space-between;
}

button.save {
  background-color: #63b47a;
  color: white;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
}

button.cancel {
  background-color: #ccc;
  color: #333;
  padding: 0.8rem 1.5rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.form-label{
  margin-bottom: 0;
}

.input-content {
  margin-bottom: 0;
}
</style>