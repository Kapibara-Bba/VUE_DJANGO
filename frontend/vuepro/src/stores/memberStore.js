import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore("member", {
  state: () => ({
    member: null, // ログインユーザー情報
    teamData: null, // Django から取得する各テーブルのデータ
  }),
  actions: {
    setUser(member) {
      this.member = member;
    },
    async fetchMemberData() {
      if (!this.member) return;

      try {
        const response = await axios.get(`http://127.0.0.1:8000/api/team/${this.member.team_id}/`);
        this.teamData = response.data;
      } catch (error) {
        console.error("チームデータの取得エラー:", error);
      }
    }
  },
  getters: {
    getMember: (state) => state.member,
    getTeamData: (state) => state.teamData,
  }
});