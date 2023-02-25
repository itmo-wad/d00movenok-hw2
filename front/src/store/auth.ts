import { defineStore } from 'pinia';
import { ref } from 'vue';

import { Profile } from '@/models/profile';

export const useAuth = defineStore('auth-store', () => {
  const isLoggedIn = ref(false);
  const profile = ref<Profile>();

  return {
    isLoggedIn,
    profile,
  };
});
