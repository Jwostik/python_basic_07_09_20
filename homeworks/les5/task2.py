'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

try:
    with open("text.txt") as f:
        content = f.readlines()
        print("Количество строк: ", len(content))
        for i, string in enumerate(content):
            print(f"Количество слов в {i + 1} строке: {len(string.split())}")
except IOError:
    print("Нет файла text.txt")
