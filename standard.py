## Create a standardized form to display data.

# To effectively standardize all medical records, we need to focus on some critical headings that all or most of the 
#   documents would have: Name, DOB, gene mutation, and additional comments given. 

# We can isolate these by looking for the keywords in the extracted text and choosing the data that follows. 

# So, for example, to look for the name, we would do the following:

exText = 'Extracted Text Name: John Doe' # We have manually set this text to a short sentence to understand the code better here.

# We can iterate through these words as such:

exText_S = exText.split()

for i in range(len(exText_S)):
  
  if 'name' in exText_S[i].lower():
    
    try:
      nameVar = str(exText_S[i + 1]) + str(exText_S[i + 2]) # [i+1] is the first name and [i+2] is the last name.
      
    except:
      
      pass #This is done to avoid index errors.
    
    
 
# Return the extracted name
    
return nameVar
