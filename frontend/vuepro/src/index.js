import { createRouter, createWebHistory } from 'vue-router';
import Login from '../src/components/MemberLogin.vue';
import Register from './components/MemberRegister.vue';

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login, // ログイン画面のコンポーネント
  },
  {
    path: '/register',
    name: 'Register',
    component: Register, // 新規登録画面のコンポーネント
    // meta: { requiresAuth: true }, // 認証が必要なルート
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 認証が必要なルートへのアクセスを保護するミドルウェア
// router.beforeEach((to, from, next) => {
//   const isAuthenticated = !!localStorage.getItem('authToken'); // ログイン状態を確認
//   if (to.meta.requiresAuth && !isAuthenticated) {
//     next('/login'); // 認証されていない場合はログイン画面へリダイレクト
//   } else {
//     next(); // それ以外の場合は次のルートへ
//   }
// });

export default router;
