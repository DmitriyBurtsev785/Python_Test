import pytest


cnt = 0

@pytest.fixture(autouse=True) # с помощью фикстуры можно генерировать какие-то данные для тестирования, с помощью параметра autouse=True запускаем в работу декоратор
def clean_text_file():
    global cnt
    with open('testfile.txt', 'w'): # очищаем файл
        pass
    print(cnt)
    cnt += 1
