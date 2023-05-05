directory = "/home/kanat/KeramaStone/KeramaStone/MainApp/static/images/products/mramor/"
import os

# указываем путь к папке
path = directory

# перебираем все файлы в папке
for filename in os.listdir(path):
    
    # проверяем, является ли файл файлом
    if os.path.isfile(os.path.join(path, filename)):
        
        # удаляем пробелы в названии файла
        os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', '')))