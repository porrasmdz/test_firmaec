import os
import re

def clean_filenames(folder_path):
    pattern = re.compile(r'^(TEST-\d+)')

    for file_name in os.listdir(folder_path):
        if not file_name.lower().endswith(".pdf"):
            continue

        match = pattern.match(file_name)
        if not match:
            print(f"No cumple patrón: {file_name}")
            continue

        new_name = f"{match.group(1)}.pdf"

        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        try:
            os.replace(old_path, new_path)  # sobrescribe si ya existe
            print(f"{file_name} -> {new_name}")
        except Exception as e:
            print(f"Error con {file_name}: {e}")
            
clean_filenames("C:\\Users\\Andres\\Downloads\\TRABAJO_FIRMASEC\\tests\\pdf_files\\original\\desk_results")