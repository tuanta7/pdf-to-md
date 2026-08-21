import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import pymupdf4llm

tk.Tk().withdraw()
pdf = filedialog.askopenfilename(title="Choose a PDF", filetypes=[("PDF files", "*.pdf")])
if pdf:
    try:
        out = Path(pdf).with_suffix(".md")
        # embed_images keeps the result a single shareable file instead of a folder
        out.write_text(pymupdf4llm.to_markdown(pdf, embed_images=True), encoding="utf-8")
        messagebox.showinfo("Done", f"Saved:\n{out}")
    except Exception as e:
        messagebox.showerror("Could not convert", str(e))
