import cv2
from fpdf import FPDF

def convert_photo_to_pdf(image_paths, output_pdf):
    # Load the image using OpenCV
    image = cv2.imread(image_paths[0])

    # Get the height and width of the image
    height, width, _ = image.shape

    # Create PDF object
    pdf = FPDF(unit="pt", format=[width, height])

    for image_path in image_paths:
      # Add a page
      pdf.add_page()

      # Set image as background
      pdf.image(image_path, 0, 0, width, height)

    # Save the PDF to file
    pdf.output(output_pdf)

# Example usage
x = int(input('Number of Images: '))
image_paths = [f'captured_image{i}' for i in range(x)]
output_pdf = "output_pdf.pdf"
convert_photo_to_pdf(image_paths, output_pdf)