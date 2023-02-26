<script setup lang="ts">
  import { io } from 'socket.io-client';

  import { useNotifications } from '@/store/notifications';

  const notificationsStore = useNotifications();
  const instance = io('', { path: '/ws/socket.io/' });

  instance.on('notify', (name: string) => {
    if (notificationsStore.notifications.indexOf(name) === -1)
      notificationsStore.notifications.push(name);
  });

  function cleanNotifications() {
    notificationsStore.notifications.splice(
      0,
      notificationsStore.notifications.length,
      ...[],
    );
  }
</script>

<template>
  <v-list rounded="lg">
    <template v-if="notificationsStore.notifications.length > 0">
      <v-list-item v-for="n in notificationsStore.notifications" :key="n" link>
        <v-list-item-title> New user: {{ n }} </v-list-item-title>
      </v-list-item>
    </template>
    <template v-else>
      <v-list-item>
        <v-list-item-title>Notifications list is empty :(</v-list-item-title>
      </v-list-item>
    </template>

    <v-divider class="my-2"></v-divider>

    <v-list-item
      link
      color="grey-lighten-4"
      @click.prevent="cleanNotifications"
    >
      <v-list-item-title> Clean </v-list-item-title>
    </v-list-item>
  </v-list>
</template>
