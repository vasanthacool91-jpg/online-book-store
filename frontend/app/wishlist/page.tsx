"use client";

import { useEffect, useState } from "react";
import api from "../lib/api";
import Navbar from "../components/Navbar";
import { useRouter } from "next/navigation";

export default function WishlistPage() {
  const [wishlist, setWishlist] = useState([]);
const router = useRouter();
  useEffect(() => {
         const token = localStorage.getItem("token");

    if (!token) {
        router.push("/login");
    }
    loadWishlist();
  }, []);

  const loadWishlist = async () => {
    const res = await api.get("/wishlist/1");
    setWishlist(res.data);
  };

  const removeWishlist = async (id: number) => {
    await api.delete(`/wishlist/${id}`);
    loadWishlist();
  };

  return (
    <>
    <Navbar />
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-5">
        My Wishlist
      </h1>

      {wishlist.map((item: any) => (
        <div
          key={item.id}
          className="border rounded p-4 mb-3 flex justify-between"
        >
          <div>
            Book ID : {item.book_id}
          </div>

          <button
            onClick={() => removeWishlist(item.id)}
            className="bg-red-500 text-white px-4 py-2 rounded"
          >
            Remove
          </button>
        </div>
      ))}
    </div>
    </>
  );
}