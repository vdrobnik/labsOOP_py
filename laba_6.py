# Создать симуляцию крокссплатформенного приложения при помощи
# паттерна «абстрактная фабрика». Фабрика должна генерировать набор
# контроллов для различных операционных систем (Windows, Linux, MacOS).
# Все контроллы наследуются от базового класса
# Contol (setPosition, getPosition).
# Примеры реализующихся контроллов и их возможных методов
# Form (addContol)
# Label (setText, getText)
# TextBox (setText, getText, OnValueChanged)
# ComboBox (getSeletecedIndex, setSelectedIndex, setItems, getItems)
# Button (setText, getText, Click)
# Приложение должно в зависимости от выбранной операционной системы
# создавать свой набор контроллов, размещать их на форме, делать с ними
# манипуляции (вызывать их методы).
# Графический интерфейс создавать не требуется! Контроллы в реальности на
# все методы просто пишут информацию о вызове метода в консоль по типу:
# «Вызван метод _____  у контролла ___»

# Погребной Владимир
# https://github.com/vdrobnik/labsOOP_py
# https://disk.yandex.ru/d/tCHxZ0RMunDLog

class AbstractFactory:
    def createForm(self):
        pass

    def createLabel(self):
        pass

    def createTextBox(self):
        pass

    def createComboBox(self):
        pass

    def createButton(self):
        pass


class WinFactory(AbstractFactory):

    def createForm(self):
        print("For Windows:")
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()


class LinuxFactory(AbstractFactory):
    def createForm(self):
        print("For Linux:")
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()


class MacFactory(AbstractFactory):

    def createForm(self):
        print("For Mac:")
        return Form()

    def createLabel(self):
        return Label()

    def createTextBox(self):
        return TextBox()

    def createComboBox(self):
        return ComboBox()

    def createButton(self):
        return Button()


class Control:
    def __init__(self):
        self.x = 0
        self.y = 0

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def getPos(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Form(Control):
    def __init__(self):
        super().__init__()
        self.controls = []

    def addControl(self, control):
        self.controls.append(control)
        print("Вызван метод addControl у контроллера Form!")



class Label(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("Вызван метод setText у конролла Label!")
        self.text = text

    def getText(self):
        print("Вызван метод getText у конролла Label!")
        print("--------------------------------------")
        return self.text


class TextBox(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        print("Вызван метод setText у конролла TextBox!")
        self.text = text

    def getText(self):
        print("Вызван метод getText у контроллов TextBox!")
        print("--------------------------------------")
        return self.text

    def onValueChanged(self):
        print("Вызван метод onValueChanged у контроллов TextBox!")
        pass


class ComboBox(Control):
    def __init__(self):
        super().__init__()
        self.items = []
        self.selectedIndex = 1

    def setItems(self, items):
        self.items = items
        print("Вызван метод setItems у контроллов ComboBox!")


    def getItems(self):
        print("Вызван метод getItems у контроллов ComboBox!")
        print("--------------------------------------")
        return self.items

    def setSelectedIndex(self, selectedIndex):
        self.selectedIndex = selectedIndex
        print("Вызван метод setSelectedIndex у контроллов ComboBox!")


    def getSelectedIndex(self):
        print("Вызван метод getSelectedIndex у контроллов ComboBox!")
        return self.selectedIndex


class Button(Control):
    def __init__(self):
        super().__init__()
        self.text = ""

    def setText(self, text):
        self.text = text
        print("Вызван метод setText у конролла  Button!")

    def getText(self):
        print("Вызван метод getText у конролла  Button!")
        print("--------------------------------------")
        return self.text


    def click(self):
        print("Вызван метод click у конролла  Button!")
        pass

if __name__ == '__main__':
    factory = WinFactory()
    # создание формы для factory
    form = factory.createForm()

    # создание контроллов
    Label = factory.createLabel()
    Label.setText("Доставка новогоднего настроения.")
    print(Label.getText())
    print("--------------------------------------")


    TextBox = factory.createTextBox()
    TextBox.setText("Выберите блюдо для Нового года!")
    print(TextBox.getText())
    print("--------------------------------------")

    ComboBox = factory.createComboBox()
    ComboBox.setSelectedIndex(2)
    ComboBox.setItems(['Оливье', 'Мандарины', 'Плов', 'Фейерверк'])
    print(ComboBox.getItems())
    print("--------------------------------------")



    Button = factory.createButton()
    Button.setText("Подтвердить заказ.")
    print(Button.getText())
    print("--------------------------------------")


    # добавление контроллов на форму
    form.addControl(TextBox)
    form.addControl(ComboBox)
    form.addControl(Label)
    form.addControl(Button)