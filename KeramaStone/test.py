import xmltodict

# чтение fb2 файла
with open("/home/kanat/KeramaStone/KeramaStone/KeramaStone/aa.fb2", "rb") as fb2_file:

# парсим содержимое файла в словарь
    book_data = xmltodict.parse(fb2_file.read())

# создаём буферный список для слов 
print(book_data)