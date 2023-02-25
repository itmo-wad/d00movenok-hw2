<script setup lang="ts">
  import { Ref, ref } from 'vue';

  import LoginForm from '@/components/LoginForm.vue';
  import RegisterForm from '@/components/RegisterForm.vue';

  const tab: Ref<number> = ref(0);
  const tabs = [
    { name: 'Login', icon: 'mdi-login' },
    { name: 'Register', icon: 'mdi-account-plus' },
  ];
</script>

<template>
  <v-card class="elevation-12" rounded="0">
    <v-tabs v-model="tab" grow>
      <v-tab v-for="(item, index) in tabs" :key="index">
        <v-icon class="pr-3">{{ item.icon }}</v-icon>
        <div class="py-2">{{ item.name }}</div>
      </v-tab>
    </v-tabs>
    <v-window v-model="tab" class="pa-4">
      <v-window-item :value="0">
        <LoginForm />
      </v-window-item>
      <v-window-item :value="1">
        <RegisterForm />
      </v-window-item>
    </v-window>
  </v-card>
</template>
