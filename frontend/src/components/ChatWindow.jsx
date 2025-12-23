// src/components/ChatWindow.jsx
import { useState } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

export default function ChatWindow() {
  const [sessionId] = useState(() =>
    (typeof crypto !== "undefined" && crypto.randomUUID)
      ? crypto.randomUUID()
      : `session-${Math.random().toString(36).slice(2)}`
  );
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hello! Ask me any coding problem 👋" },
  ]);
  const [isLoading, setIsLoading] = useState(false);

  const indent = (text, spaces = 2) =>
    text.split("\n").map((line) => " ".repeat(spaces) + line).join("\n");

  function formatBlock(title, content) {
    return `${title}:\n${indent(content)}`;
  }

  function formatComplexity(val) {
    if (!val) return "";
    if (typeof val === "string") return val;
    const parts = [];
    if (val.time) parts.push(`Time: ${val.time}`);
    if (val.space) parts.push(`Space: ${val.space}`);
    return parts.join("\n");
  }

  function formatSolution(val) {
    if (!val) return "";
    if (typeof val === "string") return val;

    const sections = [];
    if (val.description) sections.push(val.description);
    if (Array.isArray(val.steps) && val.steps.length) {
      sections.push(
        "Steps:\n" +
          val.steps
            .map((step, i) => `${i + 1}. ${step}`)
            .join("\n")
      );
    }
    if (val.code) {
      sections.push(
        "Code:\n" +
          "```python\n" +
          val.code +
          "\n```"
      );
    }

    return sections.join("\n\n");
  }

  function formatAssistantResponse(data) {
    if (data.raw_text) return data.raw_text;
    if (data.error) return data.error;

    const parts = [
      data.summary && formatBlock("Summary", typeof data.summary === "string" ? data.summary : JSON.stringify(data.summary, null, 2)),
      data.brute_force && formatBlock("Brute Force", formatSolution(data.brute_force)),
      data.optimized && formatBlock("Optimized", formatSolution(data.optimized)),
      data.complexity && formatBlock("Complexity", formatComplexity(data.complexity)),
      data.hints && formatBlock("Hints", Array.isArray(data.hints) ? data.hints.join("\n") : data.hints),
    ].filter(Boolean);

    if (Array.isArray(data.quiz) && data.quiz.length) {
      const quizText = data.quiz
        .map((q, idx) => `${idx + 1}. ${q.question} — ${q.answer}`)
        .join("\n");
      parts.push(formatBlock("Quiz", quizText));
    }

    return parts.join("\n\n") || JSON.stringify(data, null, 2);
  }

  async function sendMessage(input) {
    if (!input.trim()) return;

    // Add user message
    setMessages((prev) => [...prev, { role: "user", content: input }]);
    setIsLoading(true);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze-problem", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          problem: input,
          session_id: sessionId
        }),
      });

      const data = await response.json();

      // Add assistant message
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: formatAssistantResponse(data) },
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
