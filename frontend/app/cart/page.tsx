"use client";

import { useEffect, useState } from "react";
import api from "../lib/api";
import Navbar from "../components/Navbar";
import { useRouter } from "next/navigation";

interface CartItem {
  id: number;
  user_id: number;
  book_id: number;
  quantity: number;
}

export default function CartPage() {
  const [cartItems, setCartItems] = useState<CartItem[]>([]);
  const router = useRouter();

  useEffect(() => {
     const token = localStorage.getItem("token");

    if (!token) {
        router.push("/login");
    }
    loadCart();
  }, []);

  const loadCart = async () => {
    try {
      const res = await api.get("/cart/1");
      setCartItems(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  const removeItem = async (id: number) => {
    await api.delete(`/cart/${id}`);
    loadCart();
  };

  return (
    <>
    <Navbar />
    <div className="min-h-screen p-8 bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">My Cart</h1>

      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        cartItems.map((item) => (
          <div
            key={item.id}
            className="bg-white shadow rounded p-4 mb-4 flex justify-between items-center"
          >
            <div>
              <p><strong>Book ID:</strong> {item.book_id}</p>
              <p><strong>Quantity:</strong> {item.quantity}</p>
            </div>

            <button
              onClick={() => removeItem(item.id)}
              className="bg-red-500 text-white px-4 py-2 rounded"
            >
              Remove
            </button>
          </div>
        ))
      )}
    </div>
    </>
  );
}