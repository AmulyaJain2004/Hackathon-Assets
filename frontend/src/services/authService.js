import axios from "axios";

const API_URL = "http://localhost:8000/api/auth/";

const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add token to requests
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("access_token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      const refreshToken = localStorage.getItem("refresh_token");
      if (refreshToken) {
        try {
          // You can implement token refresh logic here if needed
          // For now, we'll just logout
          localStorage.removeItem("access_token");
          localStorage.removeItem("refresh_token");
          localStorage.removeItem("user");
          window.location.href = "/login";
        } catch (err) {
          return Promise.reject(err);
        }
      }
    }
    return Promise.reject(error);
  }
);

const authService = {
  signup: async (userData) => {
    const response = await api.post("signup/", userData);
    if (response.data.tokens) {
      localStorage.setItem("access_token", response.data.tokens.access);
      localStorage.setItem("refresh_token", response.data.tokens.refresh);
      localStorage.setItem("user", JSON.stringify(response.data.user));
    }
    return response.data;
  },

  login: async (credentials) => {
    const response = await api.post("login/", credentials);
    if (response.data.tokens) {
      localStorage.setItem("access_token", response.data.tokens.access);
      localStorage.setItem("refresh_token", response.data.tokens.refresh);
      localStorage.setItem("user", JSON.stringify(response.data.user));
    }
    return response.data;
  },

  logout: async () => {
    const refreshToken = localStorage.getItem("refresh_token");
    try {
      await api.post("logout/", { refresh_token: refreshToken });
    } catch (error) {
      console.error("Logout error:", error);
    } finally {
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      localStorage.removeItem("user");
    }
  },

  forgotPassword: async (email) => {
    const response = await api.post("forgot-password/", { email });
    return response.data;
  },

  verifyOTP: async (email, otp) => {
    const response = await api.post("verify-otp/", { email, otp });
    return response.data;
  },

  resetPassword: async (email, otp, new_password, confirm_password) => {
    const response = await api.post("reset-password/", {
      email,
      otp,
      new_password,
      confirm_password,
    });
    return response.data;
  },

  getUser: async () => {
    const response = await api.get("user/");
    return response.data;
  },

  getDashboard: async () => {
    const response = await api.get("dashboard/");
    return response.data;
  },

  getCurrentUser: () => {
    const user = localStorage.getItem("user");
    return user ? JSON.parse(user) : null;
  },

  isAuthenticated: () => {
    return !!localStorage.getItem("access_token");
  },
};

export default authService;
