import PyPDF2
import re

# file1 = open('C:/Users/Felipe/PycharmProjects/NLP/UPDATED_NLP_COURSE/00-Python-Text-Basics/Business_Proposal.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(file1)
# page2 = pdf_reader.getPage(1).extractText()
# page2_noauthors = re.findall(r'[^AUTHORS:]', page2)
# myfile = open('contacts.txt', mode='a+')
# for word in ''.join(page2_noauthors):
#     myfile.write(word)


f = open('C:/Users/Felipe/PycharmProjects/NLP/UPDATED_NLP_COURSE/00-Python-Text-Basics/Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page2 = pdf_reader.getPage(1).extractText()
f.close()
with open('contacts.txt', mode='a+') as f:
    f.write(page2[8:])
    f.seek(0)
    print(f.read())
