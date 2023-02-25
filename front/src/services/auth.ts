import { AxiosResponse } from 'axios';

import { Message } from '@/models/messages';
import { Profile } from '@/models/profile';
import { http } from '@/utils/http';

export function signin(
  login: string,
  password: string,
): Promise<AxiosResponse<Profile>> {
  return http.post('/auth/signin', {
    login,
    password,
  });
}

export function signup(
  login: string,
  password: string,
): Promise<AxiosResponse<Profile>> {
  return http.post('/auth/signup', {
    login,
    password,
  });
}

export function signout(): Promise<AxiosResponse<Message>> {
  return http.post('/auth/signed');
}
