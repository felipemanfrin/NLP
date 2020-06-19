import PyPDF2
import re

# myfile = open('C:/Users/Felipe/PycharmProjects/NLP/UPDATED_NLP_COURSE/00-Python-Text-Basics/Business_Proposal.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(myfile)
# page2 = pdf_reader.getPage(1)
# pagina2 = page2.extractText()
# print(pagina2)

#fazendo em uma só fase

f = open('C:/Users/Felipe/PycharmProjects/NLP/UPDATED_NLP_COURSE/00-Python-Text-Basics/Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page2 = pdf_reader.getPage(1).extractText()
f.close()
print(page2)
