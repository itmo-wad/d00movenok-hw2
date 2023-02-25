import { AxiosResponse } from 'axios';

import { Profile } from '@/models/profile';
import { http } from '@/utils/http';

export function getProfile(): Promise<AxiosResponse<Profile>> {
  return http.get('/profile');
}
