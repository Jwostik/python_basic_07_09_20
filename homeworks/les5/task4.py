'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One - 1
Two - 2
Three - 3
Four - 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
nums = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять",
    "Zero": "Ноль",
}

try:
    with open("text.txt") as f, open("out.txt", "w", encoding="utf-8") as out:
        for line in f:
            out.write(' '.join([nums[elem] if elem in nums.keys() else elem for elem in line.split()]) + '\n')
except IOError:
    print("Нет файла text.txt")
