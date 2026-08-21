import time
import tkinter as tk
from concurrent.futures import ThreadPoolExecutor
from tkinter import filedialog, messagebox, ttk
from pathlib import Path

import pymupdf4llm


def main():
    root = tk.Tk()
    root.withdraw()
    pdf = filedialog.askopenfilename(title="Choose a PDF", filetypes=[("PDF files", "*.pdf")])
    if not pdf:
        return

    win = tk.Toplevel(root)
    win.title("Converting")
    win.protocol("WM_DELETE_WINDOW", lambda: None)  # conversion can't be cancelled, so don't pretend
    tk.Label(win, text=f"Converting {Path(pdf).name}...").pack(padx=20, pady=(20, 10))
    bar = ttk.Progressbar(win, mode="indeterminate", length=260)
    bar.pack(padx=20, pady=(0, 20))
    bar.start(10)  # indeterminate: pymupdf4llm reports no page progress back to us

    error = None
    try:
        with ThreadPoolExecutor(max_workers=1) as ex:
            # embed_images keeps the result a single shareable file instead of a folder
            future = ex.submit(pymupdf4llm.to_markdown, pdf, embed_images=True)
            while not future.done():
                root.update()  # pump events instead of mainloop: keeps the bar animating
                time.sleep(0.05)
            out = Path(pdf).with_suffix(".md")
            out.write_text(future.result(), encoding="utf-8")
    except Exception as e:
        error = e

    win.destroy()
    if error:
        messagebox.showerror("Could not convert", str(error))
    else:
        messagebox.showinfo("Done", f"Saved:\n{out}")
    root.destroy()


if __name__ == "__main__":
    main()
