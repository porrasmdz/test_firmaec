import os
import tempfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from PIL import Image
import numpy as np
from pypdf import PdfReader, PdfWriter


def generar_pdf_grande(output_path, target_size_bytes):
    c = canvas.Canvas(output_path, pagesize=letter)
    temp_files = []
    page = 0

    try:
        while True:
            temp_img = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg").name
            temp_files.append(temp_img)

            # Generar imagen pesada
            data = np.random.randint(0, 255, (1800, 1800, 3), dtype=np.uint8)
            img = Image.fromarray(data)
            img.save(temp_img, "JPEG", quality=92)

            # Insertar en PDF
            c.drawImage(temp_img, 0, 0, width=600, height=800)
            c.showPage()
            c.save()

            size = os.path.getsize(output_path)
            print(f"[GEN] Tamaño actual: {size / (1024*1024):.4f} MB")

            if size >= target_size_bytes:
                break

            # seguir agregando páginas
            c = canvas.Canvas(output_path, pagesize=letter)
            page += 1

    finally:
        for f in temp_files:
            try:
                os.remove(f)
            except:
                pass


def unir_con_portada(portada_path, contenido_path, salida_path):
    writer = PdfWriter()

    # 1. Portada primero
    portada = PdfReader(portada_path)
    for page in portada.pages:
        writer.add_page(page)

    # 2. Luego contenido
    contenido = PdfReader(contenido_path)
    for page in contenido.pages:
        writer.add_page(page)

    # Guardar
    with open(salida_path, "wb") as f:
        writer.write(f)

    size_mb = os.path.getsize(salida_path) / (1024 * 1024)
    print(f"[FINAL] PDF generado: {salida_path}")
    print(f"[FINAL] Tamaño final: {size_mb:.4f} MB")


if __name__ == "__main__":
    # ⚙️ Configuración
    portada = "C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\test.pdf"              # tu portada
    pdf_temp = "contenido_temp.pdf"     # PDF grande sin portada
    pdf_final = "resultado_4mb.pdf"   # salida final

    # 🎯 Generar PDF de ~3.48MB (ajusta si necesitas)
    objetivo_bytes = int(3.7 * 1024 * 1024)

    print("Generando PDF base...")
    generar_pdf_grande(pdf_temp, objetivo_bytes)

    print("Uniendo con portada...")
    unir_con_portada(portada, pdf_temp, pdf_final)

    # Limpieza
    if os.path.exists(pdf_temp):
        os.remove(pdf_temp)