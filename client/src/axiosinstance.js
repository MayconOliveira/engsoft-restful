import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/api/',
});

api.interceptors.response.use(function (config) {
  return config;
}, function (error) {
    
  return Promise.reject(error);
});

export default api;