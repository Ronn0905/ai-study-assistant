// src/components/Sidebar.jsx
export default function Sidebar() {
  return (
    <aside className="w-72 bg-slate-900/80 border-r border-slate-800 flex flex-col p-4">
      <h1 className="text-xl font-semibold text-slate-50 mb-4 flex items-center gap-2">
        <span className="inline-block h-2 w-2 rounded-full bg-emerald-400" />
        AI Study Assistant
      </h1>

      <button className="mb-4 inline-flex items-center justify-center gap-2 rounded-lg bg-slate-800 hover:bg-slate-700 py-2 px-3 text-sm font-medium text-slate-100 transition">
        <span>＋</span>
        <span>New Chat</span>
      </button>

      <h2 className="text-xs font-semibold text-slate-400 uppercase tracking-wide mb-2">
        Recent
      </h2>

      <div className="space-y-1 text-sm text-slate-200">
        <button className="w-full text-left px-2 py-1.5 rounded-md hover:bg-slate-800/80">
          QuickSort Explanation
        </button>
        <button className="w-full text-left px-2 py-1.5 rounded-md hover:bg-slate-800/80">
          Two Sum Problem
        </button>
      </div>

      <div className="mt-auto pt-4 border-t border-slate-800 text-xs text-slate-500">
        <p>Backend: <span className="text-emerald-400">Connected</span></p>
        <p className="mt-1">localhost:8000</p>
      </div>
    </aside>
  );
}
