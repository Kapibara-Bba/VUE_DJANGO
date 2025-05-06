<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <h2>📝 今後の予定追加</h2>
      <input v-model="schedule_name" placeholder="タイトル" />
      <p v-if="errors.schedule_name" class="text-danger">{{ errors.schedule_name }}</p>
      <input v-model="plan_date" type="date" />
      <p v-if="errors.plan_date" class="text-danger">{{ errors.plan_date }}</p>
      <textarea v-model="notes" placeholder="備考"></textarea>
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
      schedule_name: '',
      plan_date: '',
      notes: '',
      errors: {
        schedule_name: '',
        plan_date: ''
      }
    }
  },
  methods: {
    validateCheck() {
      // タイトルのバリデーションチェック
      const title = this.schedule_name;
      if (title === '' || title === null) {
        this.errors[`schedule_name`] = 'タイトルを入力してください。';
      } else {
        this.errors[`schedule_name`] = '';
      }

      // 日にちのバリデーションチェック
      const date = this.plan_date;

      if (date === '' || date === null) {
        this.errors[`plan_date`] = '日にちを入力してください。';
      } else {
        this.errors[`plan_date`] = '';
      }
    },
    submit() {
      // バリデーションチェック
      this.validateCheck();

      // エラーがある場合は送信中止
      if (this.errors.plan_date || this.errors.schedule_name) {
        return;
      }

      const scheduleData = {
        schedule_name: this.schedule_name,
        plan_date: this.plan_date,
        notes: this.notes
      };
      this.$emit('save', scheduleData);
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
  background-color: #ffffff;
  border: 4px solid #63b47a;
  border-radius: 12px;
  padding: 2rem;
  width: 400px;
  box-shadow: 0 8px 16px rgba(0,0,0,0.3);
  font-family: 'Segoe UI', sans-serif;
}

.modal-content h2 {
  color: #063970;
  margin-bottom: 1rem;
}

input, textarea {
  width: 100%;
  margin: 0.5rem 0;
  padding: 0.8rem;
  border: 2px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
}

textarea {
  resize: vertical;
}

.buttons {
  margin-top: 1.5rem;
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
</style>