# What is a QR Code?
# A Quick Response code is a two-dimensional pictographic code used
# for its fast readability and comparatively large storage capacity.
# The code consists of black modules arranged in a square pattern
# on a white background. The information encoded can be made up of
# any kind of data (e.g., binary, alphanumeric, or Kanji symbols)

# find a solution, it doesn't work right now
# see this: https://stackoverflow.com/questions/64314649/module-qrcode-has-no-attribute-make

# Выдавало ошибку на "make". Деинсталировал все и поставил заново, затем в самом pyCharm-е выделил
# qrcode и выбрал установить qrcode, не джанго, а обычный (был вторым в списке)

# Version 1
# Создание QR-кода
import qrcode
Content_of_qr_code = 'https://t.me/ChaserTV_bot'
img = qrcode.make(Content_of_qr_code)
type(img)  # qrcode.image.pil.PilImage
print("\nThe content of the QR-code is: ", Content_of_qr_code) # "\n" - to print an empty string
img.save("ChaserTV_bot.png")

# Version 2
# import qrcode
# img = qrcode.make('Some data here')
# type(img)  # qrcode.image.pil.PilImage
# img.save("some_file.png")

# GPT answer:
# The error you are seeing is likely caused by a typo or incorrect import.
# The module qrcode does not have an attribute called 'make'. Instead, it has a function called 'make()'.
# Make sure you are importing the qrcode module correctly and then call the make() function. For example:
# import qrcode
# qrcode.make('Hello World!')

# Version 3
# import qrcode
# generate_image  =qrcode.make("test")

