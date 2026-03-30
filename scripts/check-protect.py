from pypdf import PdfReader
from pypdf.constants import UserAccessPermissions as UAP

reader = PdfReader("C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\01802-protected.pdf")

if reader.is_encrypted:
    reader.decrypt("abrir123")

    permissions = reader.trailer["/Encrypt"]["/P"]

    print("Permisos raw:", permissions)

    print("Puede imprimir:", bool(permissions & UAP.PRINT))
    print("Puede modificar:", bool(permissions & UAP.MODIFY))
    print("Puede copiar:", bool(permissions & UAP.EXTRACT))