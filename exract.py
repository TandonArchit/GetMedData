from PIL import Image
import pytesseract
from pytesseract import Output
import cv2

### First, we convert the image into grayscale.

# Image Name: ARSE.png

img = Image.open('ARSE.png').convert('L')
img.save('grey.png')


# Defining the gene to look for. This will be used later in the code.
geneMut = 'ARSE'

# A new image with the name grey.png has been saved.

### Now, we can extract the text.

baseRaw = pytesseract.image_to_string(Image.open('grey.png'))


### Now, we have the text. The second thing we need to do with the original image is highlighting the text in the image.


# The following line of code is to avoid PATH errors and specific to your computer. 

tessdata_dir_config = '--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'

# We need to convert the image data into iterable objects so, we do the following.

# Read the image file
readDt = cv2.imread('greyscale.png')

# Generate dictionary object output 
iterDic = pytesseract.image_to_data(readDt, output_type=Output.DICT, lang='eng', config=tessdata_dir_config)

# To make the overlay, we need another copy of the image, so, we do the following. 
overlay = readDt.copy()


# We are asked to report if the gene is not found, so, we set a boolean status variable. 

foundStat = False

### With all the data ready, now we can iterate over the text and look for the word.

for i in range(len(iterDic['level'])):
    
    
    # The following if condition matches words with the gene name to loacte it and highlight the name if it is found.
    
    if iterDic['text'][i] == geneMut:
      
      # We set status to True if we find the gene
     
      foundStat = True
      
      try:
        
        # We attempt to make the overlay.
        
        (x, y, w, h) = (iterDic['left'][i], iterDic['top'][i], iterDic['width'][i], iterDic['height'][i])

        (x1, y1, w1, h1) = (iterDic['left'][i + 1], iterDic['top'][i + 1], iterDic['width'][i + 1], iterDic['height'][i + 1])

        (x2, y2, w2, h2) = (iterDic['left'][i + 2], iterDic['top'][i + 2], iterDic['width'][i + 2], iterDic['height'][i + 2])

        cv2.rectangle(overlay, (x, y), (x1 + w1, y1 + h1), (255, 0, 0), -1)

        cv2.rectangle(overlay, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), -1)
      
      except Exception as ex:
        
        # If there is an error, we set the status back to not found, that is, False.
        
        foundStat = False
        
        erV = ex
        
        
## Now that our computation is done, we can form the output, if the text was found or return false if not.
        
if foundStat:
  
 try:
        
    ## Here we try to make our output image.
  
    outputImg = cv2.addWeighted(overlay, 0.2, readDt, 0.8, 0)

    return outputImg

 except:
    
    return False
    
else:
  
  return False



