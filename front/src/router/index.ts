import { storeToRefs } from 'pinia';
import { createRouter, createWebHistory } from 'vue-router';

import { useAuth } from '@/store/auth';

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/Centered.vue'),
    children: [
      {
        path: '/',
        name: 'Login',
        component: () => import('@/views/Login.vue'),
      },
    ],
  },
  {
    path: '/',
    component: () => import('@/layouts/Base.vue'),
    children: [
      {
        path: '/profile',
        name: 'Profile',
        component: () => import('@/views/Profile.vue'),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;

// Dynamic title display
router.beforeEach((to, from, next) => {
  document.title = String(to.name);
  next();
});

// Require auth
router.beforeEach((to, from, next) => {
  const { isLoggedIn } = storeToRefs(useAuth());
  if (to.name !== 'Login' && !isLoggedIn.value) {
    next({ name: 'Login' });
  } else if (to.name === 'Login' && isLoggedIn.value) {
    next({ name: 'Profile' });
  } else next();
});
