# phone = 'gosto muito da vanessa'
#
# if 'vanessa' in phone:
#     print(True)
'''r'\d{3}-\d{3}-\d{4}'# vai encontrar 3 digitos um traço depois mais 3 digitos traço depois mais 4 digitos'''

import re #importando regular expression library

# text = 'The phone number of the crush is (19)99658-6607. I need to call soon!'
# pattern = 'phone'
# print(re.search(pattern,text))
# my_match = re.search(pattern,text)#nesse padrão vai mostrar onde começa a palavra encontrada e termina
# print(my_match)
# print(my_match.span())
# my_match.start()
# my_match.end()

'''text = 'my phone is a new phone'
pattern = 'phone'
match = re.search(pattern, text)
print(match.span())
print(re.findall('phone', text))#encontro todas palavras iguais
all_matches = re.findall('phone', text)
print(len(all_matches))
for word in re.finditer('phone', text):#nessa aqui estamos pegando o começo e o fim de cada palavra desejada
    print(word.span())'''

text = 'My phone number is 19-99658-7707 and my other number is 19-99658-8808'
pattern = r'\d\d-\d\d\d\d\d-\d\d\d\d'
phonen = re.search(pattern,text)
print(phonen)
print(phonen.group())

phone2 = re.findall(r'\d\d-\d\d\d\d\d-\d\d\d\d',text)#modo resumido r'\d{3}-d{5}-d{4}'
print(phone2)
for word in re.finditer(r'\d\d-\d\d\d\d\d-\d\d\d\d',text):
    print(word.span())
for word in phone2:
    print(word)
    if '19-' in word:
        print(True)
    else:
        print(False)
