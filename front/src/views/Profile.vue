<script lang="ts" setup>
  import { storeToRefs } from 'pinia';
  import { computed, ref } from 'vue';
  import { useRouter } from 'vue-router';

  import avatar from '@/assets/default_avatar.png';
  import ChangeAvatarDialog from '@/components/ChangeAvatarDialog.vue';
  import ChangePasswordDialog from '@/components/ChangePasswordDialog.vue';
  import { signout } from '@/services/auth';
  import { editDescription } from '@/services/profile';
  import { useAuth } from '@/store/auth';

  const authStore = useAuth();
  const { isLoggedIn, cache } = storeToRefs(authStore);
  const editedDescription = ref('');
  const isEditing = ref(false);
  const error = ref('');

  const router = useRouter();

  const description = computed(() => {
    if (authStore.profile.description) {
      return authStore.profile.description;
    }
    return 'You have not created a description for your profile yet';
  });

  function setEditDescription() {
    editedDescription.value = authStore.profile.description || '';
    isEditing.value = true;
  }

  function saveDescription() {
    editDescription(editedDescription.value)
      .then(() => {
        authStore.profile.description = editedDescription.value;
        isEditing.value = false;
      })
      .catch(() => {
        error.value = 'Failed to save description!';
      });
  }

  function closeDescription() {
    editedDescription.value = '';
    isEditing.value = false;
  }

  function signOut() {
    signout().then(() => {
      isLoggedIn.value = false;
      router.push({ name: 'Login' });
    });
  }
</script>

<template>
  <div class="pa-4">
    <div class="text-h4">
      {{ authStore.profile.login }}

      <v-btn
        variant="flat"
        icon="mdi-exit-to-app"
        @click.prevent="signOut"
      ></v-btn>
    </div>

    <v-divider class="my-4"></v-divider>

    <v-row>
      <v-col cols="4">
        <v-img
          cover
          aspect-ratio="1"
          :src="
            authStore.profile.avatar
              ? `/api/profile/avatar?id=${authStore.profile.id}&cache=${cache}`
              : avatar
          "
        />
        <ChangeAvatarDialog />
        <ChangePasswordDialog />
      </v-col>
      <v-col cols="7">
        <template v-if="!isEditing">
          {{ description }}
        </template>
        <template v-else>
          <v-textarea
            v-model="editedDescription"
            class="fill-height"
            variant="solo"
            label="Description"
          ></v-textarea>
          <span class="text-caption text-error">{{ error }}</span>
        </template>
      </v-col>
      <v-col cols="1">
        <template v-if="!isEditing">
          <v-btn
            variant="flat"
            icon="mdi-pencil"
            @click.prevent="setEditDescription"
          ></v-btn>
        </template>
        <template v-else>
          <v-btn
            variant="flat"
            icon="mdi-check"
            @click.prevent="saveDescription"
          ></v-btn>
          <v-btn
            variant="flat"
            icon="mdi-window-close"
            @click.prevent="closeDescription"
          ></v-btn>
        </template>
      </v-col>
    </v-row>
  </div>
</template>
