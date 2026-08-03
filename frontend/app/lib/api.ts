import axios from "axios";

const api = axios.create({
 baseURL: "https://online-book-store-c7g4.onrender.com/",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;