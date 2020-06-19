import PyPDF2

# myfile = open('contacts.txt')
# open = myfile.read()
# print(open)

with open('contacts.txt') as f:
    fields = f.read()
    print(fields)