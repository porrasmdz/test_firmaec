from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions as UAP

src = "C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\test.pdf"
dst = "C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\01802-protected.pdf"

reader = PdfReader(src)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

permissions = UAP(0)

writer.encrypt(
    user_password="",      # contraseña para abrir el PDF
    owner_password="admin123",     # contraseña del propietario
    algorithm="AES-256",           # requiere cryptography o pycryptodome para AES
    permissions_flag=permissions,
)

with open(dst, "wb") as f:
    writer.write(f)