import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
import pytesseract
import re

# ===== WINDOWS USERS ONLY =====
# Uncomment and adjust these paths if needed:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# poppler_path = r"C:\poppler\Library\bin"

def start_ocr():
    if not pdf_path.get():
        messagebox.showerror("Error", "Please select a PDF file first.")
        return

    threading.Thread(target=process_ocr).start()

def clean_text(text):
    # Fix words split with hyphen at end of line
    text = re.sub(r'-\n', '', text)

    # Replace single line breaks inside paragraphs with space
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

    return text

def process_ocr():
    try:
        status_label.config(text="Converting PDF to images...")
        pages = convert_from_path(pdf_path.get(), dpi=400)  # add poppler_path=poppler_path if needed

        full_text = ""
        for i, page in enumerate(pages):
            status_label.config(text=f"OCR processing page {i+1}...")
            text = pytesseract.image_to_string(page, lang="ell")
            text = clean_text(text)
            full_text += text + "\n"

        output_file = os.path.splitext(pdf_path.get())[0] + "_ocr.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_text)

        status_label.config(text="Done!")
        messagebox.showinfo("Success", f"OCR completed!\nSaved to:\n{output_file}")

    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label.config(text="Error occurred.")

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_path.set(filename)


# GUI Setup
root = tk.Tk()
root.title("Simple PDF OCR Tool")
root.geometry("400x200")

pdf_path = tk.StringVar()

tk.Label(root, text="Select a PDF File:").pack(pady=10)
tk.Entry(root, textvariable=pdf_path, width=40).pack()

tk.Button(root, text="Browse", command=browse_file).pack(pady=5)
tk.Button(root, text="Start OCR", command=start_ocr).pack(pady=10)

status_label = tk.Label(root, text="Idle")
status_label.pack(pady=10)

root.mainloop()


