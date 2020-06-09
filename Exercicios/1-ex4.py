import PyPDF2

myfile = open('C:/Users/Felipe/PycharmProjects/NLP/UPDATED_NLP_COURSE/00-Python-Text-Basics/Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(myfile)
page1 = pdf_reader.getPage(1)
print(page1.extractText())