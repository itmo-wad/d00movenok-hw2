<script setup lang="ts">
  import { AxiosError } from 'axios';
  import { storeToRefs } from 'pinia';
  import { ref } from 'vue';
  import { SubmitEventPromise } from 'vuetify';

  import { Error } from '@/models/messages';
  import { editAvatar } from '@/services/profile';
  import { useAuth } from '@/store/auth';

  const authStore = useAuth();
  const { cache } = storeToRefs(authStore);

  const dialog = ref(false);
  const avatar = ref<File[]>();
  const loading = ref(false);
  const error = ref('');

  async function changePassword(event: SubmitEventPromise) {
    const results = await event;
    if (!results.valid || !avatar.value) return;

    loading.value = true;

    editAvatar(avatar.value[0])
      .then(() => {
        authStore.profile.avatar = true;
        dialog.value = false;
        // new value for avatar autoreload
        cache.value = Date.now();
      })
      .catch((e: AxiosError<Error>) => {
        console.error(e);
        if (e.response?.data.error) {
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
    Change avatar
  </v-btn>

  <v-dialog v-model="dialog" width="450px">
    <v-card>
      <v-form @submit.prevent="changePassword">
        <v-card-text>
          <v-file-input
            accept="image/*"
            label="New avatar"
            variant="underlined"
            clearable
            v-model="avatar"
          ></v-file-input>
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
