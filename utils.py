import fitz
import os

def extract_images(pdf_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    doc = fitz.open(pdf_path)

    image_paths = []

    for i in range(len(doc)):
        page = doc[i]
        images = page.get_images(full=True)

        for j, img in enumerate(images):
            xref = img[0]
            base = doc.extract_image(xref)
            image_bytes = base["image"]

            filename = f"{output_folder}/img_{i}_{j}.png"

            with open(filename, "wb") as f:
                f.write(image_bytes)

            image_paths.append(filename)

    return image_paths
