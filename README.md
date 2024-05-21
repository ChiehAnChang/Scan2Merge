# Scan2Merge
## Authors
- Chie-An
- Richie
- Kevin
- Jason

## Inspiration
For students who do not have an iPad, taking notes on paper is the norm. To address this, we developed a scanner software that allows students to take photos of their notes, scan them, and convert them into a PDF.

## What It Does
Our software enables users to use their camera to take pictures of their notes. The software then detects the paper in the images and compiles the notes into a single PDF.

## How We Built It
We primarily used Python along with libraries such as OpenCV and NumPy. Our project is divided into four parts:
1. **GUI**
2. **Camera**
3. **Transformation**
4. **PDF Conversion**

Our team consists of four members, each focusing on one part of the project.

## Challenges We Ran Into
We encountered several challenges. In the transformation part, we initially struggled to accurately capture the edges of the note paper, which made it difficult to remove background noise. Additionally, some calculations required linear algebra, so we had to consult resources to understand perspective transformation.

## Accomplishments That We're Proud Of
None of us had prior experience with OpenCV. Despite this, we managed to learn how to use OpenCV to remove the background from images within six hours and convert them into PDFs. We also successfully merged multiple PDFs into a single document. We are genuinely proud of these accomplishments.

## What We Learned
We learned how to use the OpenCV library to capture files and remove backgrounds. Additionally, we learned how to use the FPDF library to merge multiple PDFs into a single document.

## What's Next for Scan2Merge
Currently, our GUI does not support opening PDFs directly through the interface. Users need to open the PDF files from the folder manually. Enhancing the GUI to include this functionality is our next goal.


