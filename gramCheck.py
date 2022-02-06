### The following code is to check if the original file was an image of a broken or damaged record. 

## For the following extracted text: (let us manually set it to just two words for now, to understand the code.)

exText = 'Extracted Text'

## To arrive at a conclusion about the original image, we will use the following logic:

## Error Rate = (Number of words with errors) / (Number of words)

## So, the error rate will range from no errors, that is ER = 0 and complete errored, that is, ER = 1.

## To avoid false positives, the threshold will be set to 0.05, which means that if the text is more than or equal to 5% errors, the text will be tagged as faulty. 

import language_tool_python


# Initiate language 
tool = language_tool_python.LanguageTool('en-US')

# Check for error matches
try:
  
  errM = tool.check(exText)

except:
  
  return False
  
## Now we can apply our error logic
errorRate = float(len(errM)) / float(len(exText.split()))

## The error rate has been calculated and can be put up against the threshold to see if it qualifies.

if float(errorRate) >= 0.05:
  return True

else:
  return False

