import { defineStore } from 'pinia';
import { reactive, ref } from 'vue';

import { Profile } from '@/models/profile';

export const useAuth = defineStore('auth-store', () => {
  const isLoggedIn = ref(false);
  const profile: Profile = reactive({
    id: '',
    login: '',
  });
  const cache = ref(Date.now());

  return {
    isLoggedIn,
    profile,
    cache,
  };
});
