

from pyhanko.pdf_utils.reader import PdfFileReader

with open("pdf_files/win64/test-20.pdf", "rb") as f:
    reader = PdfFileReader(f)
    campos_firma = list(reader.root["/AcroForm"]["/Fields"])
    print("Cantidad de campos:", len(campos_firma))