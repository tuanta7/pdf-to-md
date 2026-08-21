# pdf-to-md

Double-click the app, pick a PDF, get a `.md` file next to it. That's the whole thing.

- First launch shows **"Windows protected your PC"** — click _More info → Run anyway_.
  The app is unsigned; that warning is normal.
- It takes a few seconds to open, and a progress bar runs while it converts. A big
  PDF takes a while — a 660-page one is about two and a half minutes. Wait for the
  "Done" box rather than double-clicking again.

## Running the script directly

```sh
uv run --python 3.12 --with pymupdf4llm python pdf_to_md.py
```
