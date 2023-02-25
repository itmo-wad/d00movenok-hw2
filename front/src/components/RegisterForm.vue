<script setup lang="ts">
  import { AxiosError } from 'axios';
  import { storeToRefs } from 'pinia';
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { SubmitEventPromise } from 'vuetify';

  import { Error } from '@/models/messages';
  import { signup } from '@/services/auth';
  import { useAuth } from '@/store/auth';

  const login = ref('');
  const password = ref('');
  const showPassword = ref(false);
  const passwordRepeat = ref('');
  const error = ref('');
  const loading = ref(false);

  function checkLogin(value: string) {
    if (value?.length > 3) return true;
    return 'Login must be at least 4 characters.';
  }

  function checkPassword(value: string) {
    if (value?.length > 8) return true;
    return 'Password must be at least 9 characters.';
  }

  function checkPassordRepeats(value: string) {
    if (value === password.value) return true;
    return 'Passwords must be equal';
  }

  const router = useRouter();

  const authStore = useAuth();
  const { isLoggedIn } = storeToRefs(authStore);
  async function signUp(event: SubmitEventPromise) {
    const results = await event;
    if (!results.valid) return;

    loading.value = true;
    error.value = '';
    signup(login.value, password.value)
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
  <v-form @submit.prevent="signUp">
    <v-text-field
      v-model="login"
      variant="underlined"
      label="Login"
      :rules="[checkLogin]"
    ></v-text-field>

    <v-text-field
      v-model="password"
      variant="underlined"
      label="Password"
      :rules="[checkPassword]"
      :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
      :type="showPassword ? 'text' : 'password'"
      @click:append="showPassword = !showPassword"
    ></v-text-field>

    <v-text-field
      v-model="passwordRepeat"
      variant="underlined"
      label="Repeat password"
      type="password"
      :rules="[checkPassordRepeats]"
    ></v-text-field>

    <span class="text-caption text-error">{{ error }}</span>

    <v-btn
      type="submit"
      block
      class="mt-2"
      :loading="loading"
      :disabled="loading"
    >
      Sign up
    </v-btn>
  </v-form>
</template>
