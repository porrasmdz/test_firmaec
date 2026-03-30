import os
from io import BytesIO

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import blue
from reportlab.pdfgen import canvas


RECT_WIDTH = 80
RECT_HEIGHT = 50
MARGIN = 20


def create_overlay(page_width: float, page_height: float) -> PdfReader:
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(page_width, page_height))

    x = page_width - RECT_WIDTH - MARGIN
    y = page_height - RECT_HEIGHT - MARGIN

    c.setStrokeColor(blue)
    c.setLineWidth(2)
    c.rect(x, y, RECT_WIDTH, RECT_HEIGHT, stroke=1, fill=0)

    c.save()
    packet.seek(0)

    return PdfReader(packet)


def add_rectangle_only_first_page(input_path: str, output_path: str) -> None:
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for i, page in enumerate(reader.pages):
        if i == 0:
            page_width = float(page.mediabox.width)
            page_height = float(page.mediabox.height)

            overlay_pdf = create_overlay(page_width, page_height)
            overlay_page = overlay_pdf.pages[0]

            page.merge_page(overlay_page)

        writer.add_page(page)

    with open(output_path, "wb") as f:
        writer.write(f)


def process_folder(folder_path: str, output_folder: str | None = None) -> None:
    if output_folder is None:
        output_folder = folder_path

    os.makedirs(output_folder, exist_ok=True)

    for file_name in os.listdir(folder_path):
        if not file_name.lower().endswith(".pdf"):
            continue

        input_path = os.path.join(folder_path, file_name)

        if not os.path.isfile(input_path):
            continue

        base, ext = os.path.splitext(file_name)
        output_path = os.path.join(output_folder, f"{base}_boxed{ext}")

        try:
            add_rectangle_only_first_page(input_path, output_path)
            print(f"Procesado: {input_path} -> {output_path}")
        except Exception as e:
            print(f"Error procesando {input_path}: {e}")


if __name__ == "__main__":
    process_folder("C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\results\\win64")