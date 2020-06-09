from datetime import datetime
#aula6
library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]

for c,v,e in library:
    print(f'{c:{10}} {v:.<30} {e:>10}')

#https://strftime.org/ para formatação de data/hora
today = datetime(year=2020,month=4,day=28)
print(f'{today:%B %d, %Y}')

"""myfile = open('UPDATED_NLP_COURSE/00-Python-Text-Basics/test.txt')
print(myfile)
print(myfile.read())
myfile.seek(0)#O cursor sai lendo letra por letra até o fim do file. Esse comandano reseta esse cursor
print('ppkinha')
print(myfile.read())
myfile.seek(0)
conteudo = myfile.read()
print(conteudo)#transfiro o conteudo para uma variavel
print('oi')
myfile.close()
print(myfile)"""


# myfile = open('UPDATED_NLP_COURSE/00-Python-Text-Basics/test.txt')
# myfile.readlines()
# myfile.seek(0)
# myline = myfile.readlines()
# print(myline)
#
# for line in myline:
#
#     if line.split()[0] == 'This':
#         print(line.split())



"""myfile = open('UPDATED_NLP_COURSE/00-Python-Text-Basics/test.txt','w+')
myfile.write('Vanessa LINDONA PORRA \n E A SHIVA TAMBEM')
myfile.seek(0)
print(myfile.readlines())
myfile.seek(0)
for frase in myfile.readlines():
    if frase.split()[0].upper() == 'VANESSA':
        print('Essa pessoa é maravilhosa')"""


with open('../UPDATED_NLP_COURSE/00-Python-Text-Basics/test.txt') as mynewfile:
    myvariable = mynewfile.readlines()
print(myvariable)



