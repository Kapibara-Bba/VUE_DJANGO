<template>
  <div class="modal-background">
    <div class="modal-content">
      <h2 class="modal-title">⚾ スケジュール編集</h2>

      <form @submit.prevent="updateSchedule">
        <div class="form-group">
          <label>タイトル</label>
          <input type="text" v-model="editedSchedule.schedule_name" required />
          <p v-if="errors.schedule_name" class="text-danger">{{ errors.schedule_name }}</p>
        </div>

        <div class="form-group">
          <label>日付</label>
          <input type="date" v-model="editedSchedule.plan_date" required />
          <p v-if="errors.plan_date" class="text-danger">{{ errors.plan_date }}</p>
        </div>

        <div class="form-group">
          <label>備考</label>
          <textarea v-model="editedSchedule.notes"></textarea>
        </div>

        <div class="modal-buttons">
          <button type="submit" class="update-btn">更新</button>
          <button type="button" class="delete-btn" @click="deleteSchedule">削除</button>
          <button type="button" class="close-btn" @click="$emit('close')">閉じる</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  emits: ['update-schedule'],
  data() {
    return {
      editedSchedule: { ...this.schedule },
      errors: {
        schedule_name: '',
        plan_date: ''
      }
    };
  },
  methods: {
    validateCheck() {
      // タイトルのバリデーションチェック
      const title = this.editedSchedule.schedule_name;
      if (title === '' || title === null) {
        this.errors[`schedule_name`] = 'タイトルを入力してください。';
      } else {
        this.errors[`schedule_name`] = '';
      }

      // 日にちのバリデーションチェック
      const date = this.editedSchedule.plan_date;

      if (date === '' || date === null) {
        this.errors[`plan_date`] = '日にちを入力してください。';
      } else {
        this.errors[`plan_date`] = '';
      }
    },
    updateSchedule() {
      // バリデーションチェック
      this.validateCheck();

      // エラーがある場合は送信中止
      if (this.errors.plan_date || this.errors.schedule_name) {
        return;
      }

      // 親コンポーネントに入力情報を渡す
      this.$emit('update-schedule', {
        schedule_id: this.editedSchedule.schedule_id,
        schedule_name: this.editedSchedule.schedule_name,
        plan_date: this.editedSchedule.plan_date,
        notes: this.editedSchedule.notes,
      });
    },
    deleteSchedule() {
      this.$emit('delete-schedule', this.editedSchedule.schedule_id);
    }
  },
  props: ['schedule'],
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
  background-color: #fff;
  padding: 30px;
  border-radius: 20px;
  width: 400px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
}

.modal-title {
  font-size: 28px;
  color: #2c3e50;
  text-align: center;
  margin-bottom: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #34495e;
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px 10px;
  border-radius: 8px;
  border: 1px solid #ccc;
}

.modal-buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
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
}

.close-btn {
  background-color: #63b47a;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 10px;
  cursor: pointer;
}
</style>
