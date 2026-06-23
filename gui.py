import tkinter as tk
from tkinter import scrolledtext, messagebox

from services.fda_client import FDAClient
from services.recall_checker import RecallChecker
from services.ai_translator import AITranslator
from storage.history import SearchHistory

client = FDAClient()
checker = RecallChecker()
translator = AITranslator()
history = SearchHistory()

def search_drug(event=None):

    drug_name = entry.get().strip()

    if not drug_name:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, "Enter a drug name.")
        return

    med = client.fetch_drug_info(drug_name)

    if med is None:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, "Drug not found or invalid input!")
        return

    text = f"""
Usage:
{med.usage}

Warnings:
{med.warnings}

Side Effects:
{med.side_effects}

Instructions:
{med.instructions}
"""

    simple = translator.simplify_text(text)

    output_box.delete(1.0, tk.END)

    if simple:
        output_box.insert(tk.END, simple)

    recall = checker.check_recall(drug_name)

    if recall:
        output_box.insert(tk.END, "\n\n⚠ RECALL WARNING ⚠\n")
        output_box.insert(tk.END, f"{recall['reason']}\n")
        output_box.insert(tk.END, f"Status: {recall['status']}\n")
        output_box.insert(tk.END, f"Date: {recall['date']}\n")

    if simple:
        history.save_search(med.name, simple)

def open_history():

    win = tk.Toplevel(window)
    win.title("Search History")
    win.geometry("400x400")
    win.configure(bg="#1e1e2f")

    history_list = history.get_history()

    box = tk.Listbox(win, bg="#2a2a40", fg="white")
    box.pack(fill="both", expand=True, padx=10, pady=10)

    for item in history_list:
        box.insert(tk.END, item["drug"])

    def clear_history():
        history.clear_history()
        box.delete(0, tk.END)

    clear_btn = tk.Button(
        win,
        text="Clear History",
        command=clear_history,
        bg="#ff4d4d",
        fg="white"
    )
    clear_btn.pack(pady=10)

    def clear_enter(e):
        clear_btn.config(bg="#ff6666")

    def clear_leave(e):
        clear_btn.config(bg="#ff4d4d")

    clear_btn.bind("<Enter>", clear_enter)
    clear_btn.bind("<Leave>", clear_leave)

window = tk.Tk()
window.title("Medication Information Translator")
window.geometry("1000x700")
window.configure(bg="#121212")

main_frame = tk.Frame(window, bg="#121212")
main_frame.pack(expand=True)

tk.Label(
    main_frame,
    text="💊 Medication Information Translator",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#121212"
).pack(pady=10)

entry = tk.Entry(
    main_frame,
    width=40,
    font=("Arial", 12),
    justify="center"
)
entry.pack(pady=10)

entry.bind("<Return>", search_drug)

def on_enter(e):
    search_btn.config(bg="#00c853")

def on_leave(e):
    search_btn.config(bg="#00a152")

search_btn = tk.Button(
    main_frame,
    text="Search",
    command=search_drug,
    bg="#00a152",
    fg="white",
    font=("Arial", 12),
    width=15
)

search_btn.pack(pady=10)

search_btn.bind("<Enter>", on_enter)
search_btn.bind("<Leave>", on_leave)

history_btn = tk.Button(
    main_frame,
    text="View History",
    command=open_history,
    bg="#2979ff",
    fg="white"
)

history_btn.pack(pady=5)

def history_enter(e):
    history_btn.config(bg="#5393ff")

def history_leave(e):
    history_btn.config(bg="#2979ff")

history_btn.bind("<Enter>", history_enter)
history_btn.bind("<Leave>", history_leave)

output_frame = tk.Frame(main_frame, bg="#121212")
output_frame.pack(pady=20, padx=25, fill="both", expand=True)

output_box = scrolledtext.ScrolledText(
    output_frame,
    width=110,
    height=25,
    bg="#1e1e2f",
    fg="white",
    font=("Consolas", 11),
    padx=20,
    pady=20
)
output_box.pack(fill="both", expand=True)

window.mainloop()