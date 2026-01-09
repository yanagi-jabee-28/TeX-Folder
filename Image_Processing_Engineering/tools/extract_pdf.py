#!/usr/bin/env python3
"""Extract text and images from a PDF and produce initial Markdown.
Usage: python tools/extract_pdf.py <path-to-pdf>
"""
from pathlib import Path
import sys
import fitz

if len(sys.argv) < 2:
    print("Usage: python tools/extract_pdf.py <path-to-pdf>")
    sys.exit(1)

pdf_path = Path(sys.argv[1])
if not pdf_path.exists():
    print(f"PDF not found: {pdf_path}")
    sys.exit(2)

out_dir = pdf_path.parent / "extracted"
images_dir = out_dir / "images"
texts_dir = out_dir / "texts"
out_dir.mkdir(exist_ok=True)
images_dir.mkdir(exist_ok=True)
texts_dir.mkdir(exist_ok=True)
md_path = out_dir / (pdf_path.stem + ".md")

print(f"Opening {pdf_path}")
doc = fitz.open(str(pdf_path))

with md_path.open("w", encoding="utf-8") as mdf:
    mdf.write(f"# {pdf_path.name}\n\n")
    for pageno in range(doc.page_count):
        page = doc.load_page(pageno)
        page_num = pageno + 1
        text = page.get_text("text")
        # Save plain text per page
        txt_file = texts_dir / f"page_{page_num:03d}.txt"
        txt_file.write_text(text, encoding="utf-8")

        mdf.write(f"## Page {page_num}\n\n")
        # Basic preservation: split lines and write paragraphs
        lines = [ln.rstrip() for ln in text.splitlines()]
        # collapse multiple empty lines
        para = []
        for ln in lines:
            if ln.strip() == "":
                if para:
                    mdf.write("\n".join(para) + "\n\n")
                    para = []
            else:
                para.append(ln)
        if para:
            mdf.write("\n".join(para) + "\n\n")

        # Extract images on this page
        img_list = page.get_images(full=True)
        if img_list:
            mdf.write(f"**Figures on page {page_num}:**\n\n")
        for img_index, img in enumerate(img_list, start=1):
            xref = img[0]
            base_image = doc.extract_image(xref)
            img_bytes = base_image["image"]
            img_ext = base_image.get("ext", "png")
            img_name = f"page_{page_num:03d}_img_{img_index}.{img_ext}"
            img_path = images_dir / img_name
            img_path.write_bytes(img_bytes)
            # Link in markdown
            rel = Path("images") / img_name
            mdf.write(
                f"![Figure {page_num}-{img_index}]({rel.as_posix()})\n\n")

print(f"Extraction complete. Outputs written to: {out_dir}")
print(f"Markdown: {md_path}")
print(f"Text files: {texts_dir}")
print(f"Images: {images_dir}")
