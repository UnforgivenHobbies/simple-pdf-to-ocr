# 📄 Simple PDF OCR (Offline Desktop GUI)

A lightweight desktop application that performs **offline Optical Character Recognition (OCR)** on PDF files using Tesseract.

This tool converts scanned PDFs into clean, UTF-8 encoded text files with support for **Greek (`ell`) and English (`eng`)** languages.

Everything runs locally on your computer.  
No cloud. No external API. No data leaves your machine.

---

# ✨ Features

- 🖥 Simple Tkinter-based GUI
- 🔒 100% Offline processing
- 📄 PDF → Image → OCR → TXT pipeline
- 🇬🇷 Greek (`ell`) support
- 🔤 Automatic word-break & hyphen cleanup
- 📈 400 DPI conversion for improved accuracy
- 🧠 Configurable Tesseract page segmentation
- 📝 UTF-8 encoded output

---

# 🏗 How It Works

The processing pipeline:

1. **PDF → Images**
   - Uses Poppler (`pdftoppm`)
   - Converts each page to image at 300 DPI

2. **OCR Extraction**
   - Uses Tesseract OCR
   - Default languages: `ell+eng`
   - Configuration:
     ```
     --psm 6
     preserve_interword_spaces=1
     ```

3. **Post-Processing**
   - Removes hyphenated line breaks
   - Merges broken lines inside paragraphs
   - Preserves paragraph spacing

4. **Export**
   - Saves output as:
     ```
     filename_ocr.txt
     ```
   - UTF-8 encoded

---

# 📦 System Requirements

- Python 3.9+
- Tesseract OCR
- Poppler
- pip (Python package manager)


# 📦 Python Packages

- pytesseract
- pdf2image
- pillow
