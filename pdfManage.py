## The following code is to generate a combined output file as a PDF.


# First, the sample data is defined.

# Name
nameVar = 'Name: ' + 'John Doe'

# Date of Birth
dob = 'DOB: ' + '01/01/01'

# Gene with the mutation
gm  = 'Gene: ' + 'ARSE'

# Extra information given
smry = 'Info: ' + ' -- SAMPLE INFO -- -- SAMPLE INFO -- -- SAMPLE INFO -- '


## Now, we can make the output PDF File

from reportlab.pdfgen.canvas import Canvas


## All the data is put on the pdf with 100 point gaps in between, to space out the data.

canvas = Canvas("output.pdf")

canvas.drawString(72, 770, nameVar)

canvas.drawString(72, 670, dob)

canvas.drawString(72, 570, gm)

canvas.drawString(72, 470, smry)


# PDF is then saved.

canvas.save()
