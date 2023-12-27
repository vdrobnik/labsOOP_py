# Нет инкапсуляции. Из-за этого ваш код может легко "вылететь"
# Погребной Владимир

# https://github.com/vdrobnik/labsOOP_py
# https://disk.yandex.ru/d/tCHxZ0RMunDLog

class Array3d:
    def __init__(self, dim0, dim1, dim2):
        self.__dim0 = dim0   #ширина
        self.__dim1 = dim1   #высота
        self.__dim2 = dim2   #глубина
        self.__length = dim0*dim1*dim2
        self.__arr = [0]*self.__length

    def __str__(self):  # Преобразовываем написание массива
        result = ""
        for i in range(self.__dim0):
            result += f"Глубина: {i}\n"
            for j in range(self.__dim1):
                for k in range(self.__dim2):
                    result += f"{self.__arr[self.transform_index(i, j, k)]} "
                result += "\n"
            result += "\n"
        return result

    @property
    def dim1(self):
        return self.__dim1

    @property
    def dim2(self):
        return self.__dim2

    @property
    def arr(self):
        return self.__arr

    def transform_index(self, i, j, k):
        return i + self.__dim0 * (j + self.__dim1 * k)  #перевод индекса

    def GetValues1(self, i):  # Получаем срез по первому приближению = двумерный массив
        result = ""
        for j in range(self.__dim1):
            result += "\n"
            for k in range(self.__dim2):
                result += f"{self.arr[self.transform_index(i, j, k)]} "
        return result

    def GetValues2(self, i, j):  # Получаем срез по второму приближению = одномерный массив
        result = ""
        for k in range(self.__dim2):
            result += f"{self.__arr[self.transform_index(i, j, k)]} "
        return result

    def SetValues1(self, i, array):  # Устанавливаем значение в массиве для заданной одной координаты (ставим необходимый двумерный массив)
        for k in range(self.__dim2):
            for j in range(self.__dim1):
                self.__arr[self.transform_index(i, j, k)] = array[k][j]
        return self.__arr

    def SetValues2(self, i, j, array):  # Устанавливаем значение в массиве для заданных двух координат (ставим необходимый одномерный массив)
        for k in range(self.__dim2):
            self.__arr[self.transform_index(i, j, k)] = array[k]
        return self.__arr

    # cоздает массив заполненный 1
    def np_ones(self):
            self.__arr = [1] * self.__length

    # cоздает массив заполненный 0
    def np_zeros(self):
            self.__arr = [0] * self.__length

    # cоздает массив заполненный определенным числом
    def np_fill(self, value):
            self.__arr = [value] * self.__length

if __name__ == '__main__':
    array = Array3d(3, 3, 3)
    array.SetValues1(0, [[1,2,3],[2,3,1],[3,1,2]])
    array.SetValues2(1, 0, [9,9,9])

    print(array.GetValues2(0, 2))
    print(array)