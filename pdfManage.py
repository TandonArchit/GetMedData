## The following code is to generate a combined output file as a PDF.

## pip install reportlab

nameVar = 'Name: ' + 'John Doe'

dob = 'DOB: ' + '01/01/01'

gm  = 'Gene: ' + 'ARSE'

smry = 'Info: ' + ' -- SAMPLE INFO -- -- SAMPLE INFO -- -- SAMPLE INFO -- '

from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("output.pdf")

canvas.drawString(72, 770, nameVar)

canvas.drawString(72, 670, dob)

canvas.drawString(72, 570, gm)

canvas.drawString(72, 470, smry)

canvas.save()
