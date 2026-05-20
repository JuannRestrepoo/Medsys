import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // tu backend FastAPI
});

export default api;