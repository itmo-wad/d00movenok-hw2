<script setup lang="ts">
  import { AxiosError } from 'axios';
  import { storeToRefs } from 'pinia';
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { SubmitEventPromise } from 'vuetify';

  import { Error } from '@/models/messages';
  import { signin } from '@/services/auth';
  import { useAuth } from '@/store/auth';

  const login = ref('');
  const password = ref('');
  const showPassword = ref(false);
  const error = ref('');
  const loading = ref(false);

  function checkNotEmpty(value: string) {
    if (value?.length > 0) return true;
    return 'Field is required';
  }

  const router = useRouter();

  const authStore = useAuth();
  const { isLoggedIn } = storeToRefs(authStore);
  async function signIn(event: SubmitEventPromise) {
    const results = await event;
    if (!results.valid) return;

    loading.value = true;
    error.value = '';
    signin(login.value, password.value)
      .then((response) => {
        isLoggedIn.value = true;
        authStore.profile = response.data;
        router.push({ name: 'Profile' });
      })
      .catch((e: AxiosError<Error>) => {
        console.error(e);
        if (e.response?.data?.error) {
          error.value = e.response?.data?.error;
        } else {
          error.value = 'Unexpected server error';
        }
      })
      .finally(() => {
        loading.value = false;
      });
  }
</script>

<template>
  <v-form @submit.prevent="signIn">
    <v-text-field
      v-model="login"
      variant="underlined"
      label="Login"
      :rules="[checkNotEmpty]"
    ></v-text-field>

    <v-text-field
      v-model="password"
      variant="underlined"
      label="Password"
      :rules="[checkNotEmpty]"
      :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
      :type="showPassword ? 'text' : 'password'"
      @click:append="showPassword = !showPassword"
    ></v-text-field>

    <span class="text-caption text-error">{{ error }}</span>

    <v-btn
      type="submit"
      block
      class="mt-2"
      :loading="loading"
      :disabled="loading"
    >
      Sign in
    </v-btn>
  </v-form>
</template>
