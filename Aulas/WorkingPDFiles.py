import PyPDF2

myfile = open('../UPDATED_NLP_COURSE/00-Python-Text-Basics/US_Declaration.pdf', mode='rb')
# pdf_reader = PyPDF2.PdfFileReader(myfile)
# print(pdf_reader.numPages)
# page1 = pdf_reader.getPage(0)
# print(page1.extractText())
# mytext = page1.extractText()
# print('oioi')
# print(mytext)

"""pdf_reader = PyPDF2.PdfFileReader(myfile)
page1 = pdf_reader.getPage(0)
print(page1.extractText())
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page1)
pdf_output = open('MY_BRAND_NEW.pdf', mode='wb')
pdf_writer.write(pdf_output)
pdf_output.close()
myfile.close()"""

# new = open('MY_BRAND_NEW.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(new)
# pdf_reader.getPage(0)
# print(pdf_reader.numPages)

pdf_list = []
pdf_reader = PyPDF2.PdfFileReader(myfile)
for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_list.append(page.extractText())


print(len(pdf_list))
for page in pdf_list:
    print(page)
    print('\n')
    print('\n')
    print('\n')

