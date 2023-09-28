import tkinter as tk
from tkinter import ttk
from difflib import SequenceMatcher

def similarity_ratio(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

def check_plagiarism():
    text1 = text_box1.get("1.0", "end-1c")
    text2 = text_box2.get("1.0", "end-1c")

    similarity = similarity_ratio(text1, text2)

    result_label.config(text=f"Similarity: {similarity * 100:.2f}%")

app = tk.Tk()
app.title("Plagiarism Checker")

frame1 = ttk.LabelFrame(app, text="Original Text")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame2 = ttk.LabelFrame(app, text="Checked Text")
frame2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

text_box1 = tk.Text(frame1, width=40, height=10)
text_box1.pack(fill="both", expand=True)

text_box2 = tk.Text(frame2, width=40, height=10)
text_box2.pack(fill="both", expand=True)

check_button = ttk.Button(app, text="Check Plagiarism", command=check_plagiarism)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = ttk.Label(app, text="", font=("Helvetica", 12))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()
