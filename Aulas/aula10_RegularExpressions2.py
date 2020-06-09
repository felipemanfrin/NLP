import re

# text = 'my phone number is 19-94235-1234'
# pattern = r'(\d{2})-(\d{5})-(\d{4})'
# mymatch = re.search(pattern, text)
# print(mymatch)
# print(mymatch.group())
# print(mymatch.group(1))

'''print(re.search(r'man|woman','This woman was here'))
print(re.findall(r'.at','the cat in the hat sat splat'))#aqui ele eta pegando somente um caracter a mais do que ele esta buscando no seu print
# ^ começa com
# $ termina com
print(re.findall(r'\d$','23423 This ends with a numer 2234234'))
print(re.findall(r'^\d','1123123 is the first number primo 235667'))
# r'[^\d]' quando tem o [^] ele vai excluir o digito que estiver selecionado dentro dele
frase = 'There are 3 number 34 insede 5 this sentence'
print(re.findall(r'[^\d]', frase)) # ou seja ele excluio os numeros 3 34 e 5
print(re.findall(r'[^\d]+',frase)) #impreme sem os numeros em conjuntos e não por letras'''

# frase = 'Gosto muito de LOTR'
# print(frase.split())
# for palavra in frase.split():
#     for letra in palavra:
#         print(letra)

'''text_phrase = 'This is a string! but it has puncutation. How to remove it?'
mylist = re.findall(r'[^!.?]+', text_phrase)
print(mylist)
print(' '.join(mylist))'''

text = 'Only find the hypen-words. Were the long-ish dash words?'
print(re.findall(r'[\w]+-[\w]+',text))# quando nao tem o ^ dentro do [] voce procupra por um numero x de paramentros que voce colocou dentro do []. não preciso especificar o tamanho da string que busco