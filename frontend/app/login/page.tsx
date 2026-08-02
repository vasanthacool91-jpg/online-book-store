"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import api from "../lib/api";

export default function LoginPage() {
  const router = useRouter();

  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const login = async () => {
    try {
      const res = await api.post("/auth/login", form);

      localStorage.setItem("token", res.data.access_token);

      alert("Login Successful");

      router.push("/books");
    } catch (err: any) {
      alert(err.response?.data?.detail || "Login Failed");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="bg-white p-8 rounded-xl shadow-lg w-96">

        <h1 className="text-3xl font-bold mb-6 text-center">
          Login
        </h1>

        <input
          className="w-full border p-3 rounded mb-3"
          placeholder="Email"
          onChange={(e) =>
            setForm({ ...form, email: e.target.value })
          }
        />

        <input
          type="password"
          className="w-full border p-3 rounded mb-5"
          placeholder="Password"
          onChange={(e) =>
            setForm({ ...form, password: e.target.value })
          }
        />

        <button
          onClick={login}
          className="w-full bg-green-600 text-white p-3 rounded"
        >
          Login
        </button>

      </div>
    </div>
  );
}