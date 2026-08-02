"use client";

import { useEffect, useState } from "react";
import api from "../lib/api";
import Navbar from "../components/Navbar";
import { useRouter } from "next/navigation";
interface Book {
  id: number;
  title: string;
  author: string;
  category: string;
  price: number;
  description: string;
  image: string;
}

export default function BooksPage() {
  const [books, setBooks] = useState<Book[]>([]);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
        router.push("/login");
    }
    loadBooks();
  }, []);

  const loadBooks = async () => {
    try {
      const res = await api.get("/books");
      setBooks(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  const addToWishlist = async (bookId: number) => {
  try {
    await api.post("/wishlist", {
      user_id: 1,
      book_id: bookId,
    });

    alert("Added to Wishlist");
  } catch (err) {
    console.error(err);
  }
};


const addToCart = async (bookId: number) => {
  try {
    await api.post("/cart/", {
      user_id: 1,
      book_id: bookId,
      quantity: 1,
    });

    alert("Book added to cart");
  } catch (error) {
    console.error(error);
    alert("Failed to add to cart");
  }
};

  return (
    <>
  <Navbar />
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-bold mb-6">Online Book Store</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {books.map((book) => (
          <div
            key={book.id}
            className="bg-white rounded-xl shadow-md p-5"
          >
            <img
              src={book.image}
              alt={book.title}
              className="w-full h-56 object-cover rounded"
            />

            <h2 className="text-xl font-semibold mt-3">
              {book.title}
            </h2>

            <p>{book.author}</p>

            <p>{book.category}</p>

            <p className="font-bold text-green-700">
              ₹{book.price}
            </p>

           <button
            onClick={() => addToWishlist(book.id)}
            className="mt-3 w-full bg-blue-600 text-white p-2 rounded"
            >
            Add to Wishlist
        </button>

            <button
  onClick={() => addToCart(book.id)}
  className="w-full mt-2 bg-green-600 text-white py-2 rounded"
>
  🛒 Add to Cart
</button>
          </div>
        ))}
      </div>
    </div>
    </>
  );
}