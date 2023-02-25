import axios, {
  AxiosError,
  AxiosInstance,
  AxiosRequestConfig,
  AxiosResponse,
} from 'axios';
import { storeToRefs } from 'pinia';

import { useAuth } from '@/store/auth';

class Http {
  private instance: AxiosInstance;

  public constructor(base: string) {
    this.instance = axios.create({
      baseURL: `${base}`,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    this.instance.interceptors.response.use(
      this.handleResponse,
      this.handleError,
    );
  }

  public request<T = any, R = AxiosResponse<T>>(
    config: AxiosRequestConfig,
  ): Promise<R> {
    return this.instance.request<T, R>(config);
  }

  public get<T = any, R = AxiosResponse<T>>(
    url: string,
    config?: AxiosRequestConfig,
  ): Promise<R> {
    return this.instance.get<T, R>(url, config);
  }

  public post<T = any, R = AxiosResponse<T>>(
    url: string,
    data?: any,
    config?: AxiosRequestConfig,
  ): Promise<R> {
    return this.instance.post<T, R>(url, data, config);
  }

  public put<T = any, R = AxiosResponse<T>>(
    url: string,
    data?: any,
    config?: AxiosRequestConfig,
  ): Promise<R> {
    return this.instance.put<T, R>(url, data, config);
  }

  public delete<T = any, R = AxiosResponse<T>>(
    url: string,
    config?: AxiosRequestConfig,
  ): Promise<R> {
    return this.instance.delete<T, R>(url, config);
  }

  // eslint-disable-next-line class-methods-use-this
  protected handleResponse(response: AxiosResponse): AxiosResponse<any> {
    return response;
  }

  // eslint-disable-next-line class-methods-use-this
  protected handleError(err: AxiosError): Promise<never> {
    if (err.response?.status === 403) {
      const { isLoggedIn } = storeToRefs(useAuth());
      isLoggedIn.value = false;
    }

    return Promise.reject(err);
  }
}

export const http = new Http('/api');
