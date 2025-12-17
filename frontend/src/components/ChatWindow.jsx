// src/components/ChatWindow.jsx
import { useState } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

export default function ChatWindow() {
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hello! Ask me any coding problem 👋" },
  ]);
  const [isLoading, setIsLoading] = useState(false);

  async function sendMessage(input) {
    if (!input.trim()) return;

    // Add user message
    setMessages((prev) => [...prev, { role: "user", content: input }]);
    setIsLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze-problem", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ problem: input }),
      });

      const data = await response.json();

      // Add assistant message
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: data.summary || JSON.stringify(data) },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "⚠️ Error contacting backend." },
      ]);
    }

    setIsLoading(false);
  }

  return (
    <div className="flex-1 flex flex-col bg-slate-900">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((msg, i) => (
          <MessageBubble
            key={i}
            role={msg.role}
            content={msg.content}
          />
        ))}

        {isLoading && (
          <div className="text-slate-300 italic">Thinking…</div>
        )}
      </div>

      {/* Input */}
      <ChatInput onSend={sendMessage} isLoading={isLoading} />
    </div>
  );
}
