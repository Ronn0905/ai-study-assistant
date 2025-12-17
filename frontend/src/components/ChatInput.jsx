// src/components/ChatInput.jsx
import { useState } from "react";

export default function ChatInput({ onSend, isLoading }) {
  const [input, setInput] = useState("");

  function handleSend() {
    if (!input.trim()) return;
    onSend(input);   // send text to ChatWindow
    setInput("");    // clear box
  }

  function handleKeyDown(e) {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }

  return (
    <div className="border-t border-slate-800 bg-slate-900/80 p-3">
      <div className="mx-auto max-w-3xl flex gap-2">
        <textarea
          className="flex-1 max-h-40 min-h-[52px] resize-none rounded-xl bg-slate-900 border border-slate-700 px-3 py-2 text-sm text-slate-100 shadow-inner focus:outline-none focus:ring-2 focus:ring-blue-500/60 focus:border-blue-500/60"
          placeholder="Ask me any coding question… (Shift+Enter for new line)"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
        />

        <button
          onClick={handleSend}
          disabled={isLoading || !input.trim()}
          className="rounded-xl bg-blue-600 hover:bg-blue-500 disabled:bg-slate-700 disabled:cursor-not-allowed px-4 text-sm font-medium text-white flex items-center gap-2 shadow-sm transition"
        >
          {isLoading ? (
            <span className="animate-pulse">Thinking…</span>
          ) : (
            <>
              <span>Send</span>
              <span>➤</span>
            </>
          )}
        </button>
      </div>

      <p className="mt-1 text-[11px] text-slate-500 text-center">
        Enter = send · Shift+Enter = new line
      </p>
    </div>
  );
}
