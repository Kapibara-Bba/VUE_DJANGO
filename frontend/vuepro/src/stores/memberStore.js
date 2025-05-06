import { defineStore } from "pinia";
// import axios from "axios";

export const useMemberStore = defineStore("member", {
  state: () => ({
    member: null, // ログインユーザー情報
    teamData: null, // Django から取得する各テーブルのデータ
  }),
  actions: {
    setData(member, team) {
      this.member = member;
      this.teamData = team;
    },
  },
  getters: {
    getMember: (state) => state.member,
    getTeamData: (state) => state.teamData,
  }
});