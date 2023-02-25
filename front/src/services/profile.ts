import { AxiosResponse } from 'axios';

import { Error, Message } from '@/models/messages';
import { Profile } from '@/models/profile';
import { http } from '@/utils/http';

export function getProfile(): Promise<AxiosResponse<Profile>> {
  return http.get('/profile');
}

export function editDescription(
  description: string,
): Promise<AxiosResponse<Error | Message>> {
  return http.put('/profile/description', { description });
}

export function editPassword(
  oldPassword: string,
  newPassword: string,
): Promise<AxiosResponse<Error | Message>> {
  return http.put('/profile/password', {
    old_password: oldPassword,
    new_password: newPassword,
  });
}

export function editAvatar(
  avatar: File,
): Promise<AxiosResponse<Error | Message>> {
  const formData = new FormData();
  formData.append('avatar', avatar);

  return http.put('/profile/avatar', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
}
