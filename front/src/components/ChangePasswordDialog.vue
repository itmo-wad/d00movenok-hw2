<script setup lang="ts">
  import { AxiosError } from 'axios';
  import { ref } from 'vue';
  import { SubmitEventPromise } from 'vuetify';

  import { Error } from '@/models/messages';
  import { editPassword } from '@/services/profile';

  const dialog = ref(false);
  const oldPassowrd = ref('');
  const showOldPassword = ref(false);
  const newPassowrd = ref('');
  const showNewPassword = ref(false);
  const passwordRepeat = ref('');
  const loading = ref(false);
  const error = ref('');

  function checkNotEmpty(value: string) {
    if (value?.length > 0) return true;
    return 'Field is required';
  }

  function checkPassword(value: string) {
    if (value?.length > 8) return true;
    return 'Password must be at least 9 characters.';
  }

  function checkPassordRepeats(value: string) {
    if (value === newPassowrd.value) return true;
    return 'Passwords must be equal';
  }

  async function changePassword(event: SubmitEventPromise) {
    const results = await event;
    if (!results.valid) return;

    loading.value = true;

    editPassword(oldPassowrd.value, newPassowrd.value)
      .then(() => {
        dialog.value = false;
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
  <v-btn @click="dialog = true" class="mt-4" variant="outlined" block>
    Change password
  </v-btn>

  <v-dialog v-model="dialog" width="450px">
    <v-card>
      <v-form @submit.prevent="changePassword">
        <v-card-text>
          <v-text-field
            v-model="oldPassowrd"
            variant="underlined"
            label="Old password"
            :rules="[checkNotEmpty]"
            :append-icon="showOldPassword ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showOldPassword ? 'text' : 'password'"
            @click:append="showOldPassword = !showOldPassword"
          ></v-text-field>

          <v-text-field
            v-model="newPassowrd"
            variant="underlined"
            label="New password"
            :rules="[checkPassword]"
            :append-icon="showNewPassword ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showNewPassword ? 'text' : 'password'"
            @click:append="showNewPassword = !showNewPassword"
          ></v-text-field>

          <v-text-field
            v-model="passwordRepeat"
            variant="underlined"
            label="Repeat password"
            type="password"
            :rules="[checkPassordRepeats]"
          ></v-text-field>
          <span class="text-caption text-error">{{ error }}</span>
        </v-card-text>
        <v-card-actions>
          <v-btn block type="submit" :loading="loading" :disabled="loading">
            Submit
          </v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>
