// src/HomePage.jsx
import Sidebar from "./components/Sidebar";
import ChatWindow from "./components/ChatWindow";

export default function HomePage() {
  return (
    <div className="h-screen w-screen flex bg-slate-900 text-slate-100">
      <Sidebar />
      <ChatWindow />
    </div>
  );
}
