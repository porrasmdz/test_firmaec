from pypdf import PdfReader, PdfWriter


def add_cover_to_pdf(cover_path, input_pdf, output_pdf):
    writer = PdfWriter()

    # leer portada
    cover = PdfReader(cover_path)
    cover_page = cover.pages[0]

    # agregar portada
    writer.add_page(cover_page)

    # leer documento original
    reader = PdfReader(input_pdf)

    for page in reader.pages:
        writer.add_page(page)

    # guardar
    with open(output_pdf, "wb") as f:
        writer.write(f)
        
add_cover_to_pdf("C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\test.pdf", 
                 "C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\032-test-1gb.pdf", 
                 "C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\032-test-1gb-cov.pdf")
add_cover_to_pdf("C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\test.pdf", 
                 "C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\033-test-1_5gbs.pdf", 
                 "C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\033-test-1_5gbs-cov.pdf")