# Создаем список из числел
array = list(map(int, input("Введите числа через пробел: ").split()))
print(array)


# Сортируем "пузырьком"
def sortArray():
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


# показываем отсортированныей список
print(sortArray())
# вводим число
num = int(input('Теперь введите число:'))


# находим  положение в списке
def binary_search(array, num, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == num:
        return middle - 1
    elif num < array[middle]:
        return binary_search(array, num, left, middle - 1)
    else:
        return binary_search(array, num, middle + 1, right)


if num == min(array) or num == max(array):
    print("Ошибка")

print(binary_search(sorted(array), num, 0, len(array)))
