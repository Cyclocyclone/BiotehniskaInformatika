from encryptText import encryptText
from decryptText import decryptText

i_text = 'Biomedicinska informatika'
i_key = 'enkripcija'

eText = encryptText(i_text, i_key)
print(eText)


i=0
j=0
k=0
Kljuc = ['x','x','x']
znaki = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

eText = 'q9rOgtbXgt3by9bWx9iJxNzV0NbUw6eJrM7Xx+eJsNzfw9ikgrHK1uLWgt/YzODd2M6jgp6bkKSXk6aflC' #Šifropis
beseda = 'Janez' #iskana beseda

for i in range(len(znaki)):
    Kljuc[0] = znaki[i]
    for j in range(len(znaki)):
        Kljuc[1] = znaki[j]
        for k in range(len(znaki)):
            Kljuc[2] = znaki[k]
            dText = decryptText(eText, Kljuc)
            if beseda in dText:
                print(Kljuc)
                print(dText)
                break
            