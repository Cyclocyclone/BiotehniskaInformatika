from encryptText import encryptText
from decryptText import decryptText

i_text = 'Biomedicinska_informatika'
i_key = 'kljuc'

eText = encryptText(i_text, i_key)
print(eText)

dText = decryptText(eText, i_key)
print(dText)

#naloga

i_text = 'Biomedicinska informatika'
i_key = 'enkripcija'

eText = encryptText(i_text, i_key)
print(eText)
