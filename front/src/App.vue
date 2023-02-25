<script setup lang="ts">
  import { storeToRefs } from 'pinia';
  import { onMounted } from 'vue';
  import { useRouter } from 'vue-router';

  import { getProfile } from '@/services/profile';
  import { useAuth } from '@/store/auth';

  const router = useRouter();
  const { isLoggedIn, profile } = storeToRefs(useAuth());

  onMounted(() => {
    getProfile().then((response) => {
      isLoggedIn.value = true;
      profile.value = response.data;
      router.push({ name: 'Profile' });
    });
  });
</script>

<template>
  <v-app>
    <router-view />
  </v-app>
</template>
