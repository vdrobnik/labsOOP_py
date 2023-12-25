# Создать класс Array3d, который будет представлять трехмерный массив, но на самом деле будет хранить данные в одномерном массиве. Вот список методов, которые нужно реализовать:
# Создание экземпляра класса Array3d с заданными размерами (dim0, dim1, dim2)
# Индексатор для доступа к элементам массива по трехмерным координатам (i, j, k)
# Метод GetValues0(int i): возвращает срез массива по первой координате (i, .., ..).
# Метод GetValues1(int j): возвращает срез массива по второй координате (.., j, ..).
# Метод GetValues2(int k): возвращает срез массива по третьей координате (.., .., k).
# Метод GetValues01(int i, int j): возвращает срез массива по первой и второй координатам (i, j, ..)
# Метод GetValues02(int i, int k): возвращает срез массива по первой и третьей координатам (i, .., k)
# Метод GetValues12(int j, int k): возвращает срез массива по второй и третьей координатам (.., j, k)
# Метод SetValues0(int i, [][]): устанавливает значения в массиве для заданной первой координаты
# Метод SetValues1(int j, [][]): устанавливает значения в массиве для заданной второй координаты
# Метод SetValues2(int k, [][]): устанавливает значения в массиве для заданной третьей координаты
# Метод SetValues01(int i, int j, [][]): устанавливает значения в массиве для заданных первой и второй координат
# Метод SetValues02(int i, int k, [][]): устанавливает значения в массиве для заданных первой и третьей координат
# Метод SetValues12(int j, int k, [][]): устанавливает значения в массиве для заданных второй и третьей координат
# Методы для создания массива с одинаковыми элементами: np.ones, np.zeros, np.fill

# Погребной Владимир
# https://github.com/vdrobnik/labsOOP_py
# https://disk.yandex.ru/d/tCHxZ0RMunDLog

class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self.dim0 = dim0   #ширина
        self.dim1 = dim1   #высота
        self.dim2 = dim2   #глубина
        self.length = dim0*dim1*dim2
        self.arr = [0]*self.length

    def __str__(self):  # Преобразовываем написание массива
        result = ""
        for i in range(self.dim0):
            result += f"Глубина: {i}\n"
            for j in range(self.dim1):
                for k in range(self.dim2):
                    result += f"{self.arr[self.transform_index(i, j, k)]} "
                result += "\n"
            result += "\n"
        return result

    def transform_index(self, i, j, k):
        return i + self.dim0 * (j + self.dim1 * k)#перевод индекса

    def GetValues1(self, i):  # Получаем срез по первому приближению - двумерный массив
        result = ""
        for j in range(self.dim1):
            result += "\n"
            for k in range(self.dim2):
                result += f"{self.arr[self.transform_index(i, j, k)]} "
        return result

    def GetValues2(self, i, j):  # Получаем срез по второму приближению - одномерный массив
        result = ""
        for k in range(self.dim2):
            result += f"{self.arr[self.transform_index(i, j, k)]} "
        return result

    def SetValues1(self, i, array):  # Устанавливаем значение в массиве для заданной одной координаты (ставим необходимый двумерный массив)
        for k in range(self.dim2):
            for j in range(self.dim1):
                self.arr[self.transform_index(i, j, k)] = array[k][j]
        return self.arr

    def SetValues2(self, i, j, array):  # Устанавливаем значение в массиве для заданных двух координат (ставим необходимый одномерный массив)
        for k in range(self.dim2):
            self.arr[self.transform_index(i, j, k)] = array[k]
        return self.arr
        # Создает массив единиц
    def np_ones(self):
            self.arr = [1] * self.length
        # Создает массив заполненный 0
    def np_zeros(self):
            self.arr = [0] * self.length
        # Создает массив заполненный определенным числом
    def np_fill(self, value):
            self.arr = [value] * self.length

if __name__ == '__main__':
    array = Array3d(3, 3, 3)
    array.SetValues1(0, [[5,2,3],[2,3,5],[3,5,2]])
    array.SetValues2(1, 0, [9,9,9])

    print(array.GetValues2(0, 2))
    print(array)