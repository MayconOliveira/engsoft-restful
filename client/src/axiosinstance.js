import axios from 'axios';

const api = axios.create({
  baseURL: 'https://api.wevalue.com.br/api/',
});

api.interceptors.response.use(function (config) {
  return config;
}, function (error) {
    
  return Promise.reject(error);
});

export default api;