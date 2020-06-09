import PyPDF2

file1 = open('C:/Users/Felipe/PycharmProjects/NLP/UPDATED_NLP_COURSE/00-Python-Text-Basics/Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(file1)
page2 = pdf_reader.getPage(1)
print(page2.extractText())
for x in page2.extractText():
    print(x)

