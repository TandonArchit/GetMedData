# Get Med Data
Extract data from medical files.

## Installs required:
**!sudo apt install tesseract-ocr** \
**!pip install pytesseract** \
**pip install language_tool_python** \
**pip install PyPDF2** \
**pip install reportlab**


## How the code works:

**Step 1:** The original image is converted into grayscale and saved as a new image. The new image is then read, and text is extracted using Tesseract OCR. This is the initial step where the first attempt is made to read the text and return the text.

**Step 2:** Here, there are two possibilities. One that the original image was clean. The other that the original image is a picture of an old record that might have had some physical damage to the paper, resulting in incorrect OCR output. So, to check if there were inaccurate readings, we will check for grammatical errors in the text. A high error rate would indicate issues with the original image. 

**Step 3:** Now that we have our clean text, we can search for the variant name and highlight it on the image. 

**Step 4:** Make a standardized presentation format for all the images to make it easier to understand.

**Step 5:** Put a final output together with the original image, image with highlights and the standardized form of data in a PDF file.

## Output Text

You can see the actual output text of the code, saved in the text file.
