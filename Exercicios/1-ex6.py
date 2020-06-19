import re
import PyPDF2


f = open('C:/Users/Felipe/PycharmProjects/NLP/UPDATED_NLP_COURSE/00-Python-Text-Basics/Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page2 = pdf_reader.getPage(1).extractText()
print(re.findall('[\w]+@[\w]+.com', page2))