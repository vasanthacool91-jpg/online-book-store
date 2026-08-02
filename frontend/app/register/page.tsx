"use client";

import { useState } from "react";
import api from "../lib/api";

export default function RegisterPage() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
  });

  const register = async () => {
    try {
      const res = await api.post("/auth/register", form);
      alert("Registration Successful");
      console.log(res.data);
      router.push("/login");
    } catch (err: any) {
      alert(err.response?.data?.detail || "Registration Failed");
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-96 bg-white p-8 rounded-xl shadow-lg">
        <h1 className="text-3xl font-bold text-center mb-6">
          Register
        </h1>

        <input
          className="w-full border p-3 rounded mb-3"
          placeholder="Name"
          onChange={(e) =>
            setForm({ ...form, name: e.target.value })
          }
        />

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
          onClick={register}
          className="w-full bg-blue-600 text-white p-3 rounded hover:bg-blue-700"
        >
          Register
        </button>
      </div>
    </div>
  );
}