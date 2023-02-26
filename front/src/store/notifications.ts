import { defineStore } from 'pinia';
import { reactive } from 'vue';

export const useNotifications = defineStore('notifications-store', () => {
  const notifications: string[] = reactive([]);

  return {
    notifications,
  };
});
