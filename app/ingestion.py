import fitz  
from app.vector_db import store_chunks

async def ingest_pdf(file):
    contents = await file.read()
    pdf = fitz.open(stream=contents, filetype="pdf")
    toc = pdf.get_toc()
 
    if not toc:
        toc = []
        for page_num, page in enumerate(pdf, start=1):
            first_line = page.get_text("text").split('\n')[0].strip()
            if first_line and not first_line.isdigit() and len(first_line) > 3:
                toc.append(f"Page {page_num}: {first_line}")

    pages = [page.get_text() for page in pdf]
    for i, page in enumerate(pages):
        store_chunks([page], metadata={"page_num": i + 1})

    return toc, pages