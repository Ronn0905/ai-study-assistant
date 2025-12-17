// src/components/MessageBubble.jsx
export default function MessageBubble({ role, content }) {
  const isUser = role === "user";

  return (
    <div
      className={`flex ${isUser ? "justify-end" : "justify-start"} animate-[fadeIn_0.15s_ease-out]`}
    >
      <div
        className={`max-w-2xl rounded-2xl px-4 py-3 text-sm shadow-sm
        ${isUser
          ? "bg-blue-600 text-white"
          : "bg-slate-800 text-slate-50 border border-slate-700"
        }`}
      >
        {!isUser && (
          <p className="text-xs font-semibold text-emerald-300 mb-1">
            Assistant
          </p>
        )}
        {isUser && (
          <p className="text-xs font-semibold text-blue-100 mb-1">
            You
          </p>
        )}
        <p className="whitespace-pre-wrap leading-relaxed">{content}</p>
      </div>
    </div>
  );
}
