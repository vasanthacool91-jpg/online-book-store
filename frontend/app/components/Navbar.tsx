"use client";

import Link from "next/link";
import { useRouter } from "next/navigation";

export default function Navbar() {
  const router = useRouter();

  const logout = () => {
    localStorage.removeItem("token");
    router.push("/login");
  };

  return (
    <nav className="bg-blue-600 text-white shadow-md">
      <div className="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">

        <Link
          href="/books"
          className="text-2xl font-bold"
        >
          📚 Book Store
        </Link>

        <div className="flex gap-6 items-center">

          <Link href="/books">
            Books
          </Link>

          <Link href="/wishlist">
            Wishlist
          </Link>

          <Link href="/cart">
            Cart
          </Link>

          <button
            onClick={logout}
            className="bg-red-500 px-4 py-2 rounded hover:bg-red-600"
          >
            Logout
          </button>

        </div>

      </div>
    </nav>
  );
}