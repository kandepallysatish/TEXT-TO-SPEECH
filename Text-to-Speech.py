import pyttsx3
import PyPDF2

book = open('Batch No 01.pdf', 'rb')  # ENTER YOUR FILE PDF HERE
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

speaker = pyttsx3.init()  # MODULE USE

#  from specified pages
for num in range(1, 5):   # HERE WE SPECIFIED TO SPEACK FROM 1 TO 5 PAGES

    page = pdfReader.getPage(1)  # SPECIFIES PAGES NUMBER WHILE RUNNING
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()