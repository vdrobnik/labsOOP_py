import tkinter as tk
from tkinter import ttk

class Control:
    def setPosition(self):
        print(f"Вызван метод setPosition у контролла {type(self).__name__}")

    def getPosition(self):
        print(f"Вызван метод getPosition у контролла {type(self).__name__}")

    def OnValueChanged(self):
        print(f"Вызван метод OnValueChanged у контролла {type(self).__name__}")

    def getSelectedIndex(self):
        print(f"Вызван метод getSelectedIndex у контролла {type(self).__name__}")

    def setSelectedIndex(self, index):
        print(f"Вызван метод setSelectedIndex у контролла {type(self).__name__}")

    def setItems(self, items):
        print(f"Вызван метод setItems у контролла {type(self).__name__}")

    def getItems(self):
        print(f"Вызван метод getItems у контролла {type(self).__name__}")

    def Click(self):
        print(f"Вызван метод Click у контролла {type(self).__name__}")

    def setText(self, text):
        print(f"Вызван метод setText у контролла {type(self).__name__}")

    def getText(self):
        print(f"Вызван метод getText у контролла {type(self).__name__}")

    def addControl(self):
        print(f"Вызван метод addControl у контролла {type(self).__name__}")

#эти классы не переопределяют методы
class WindowsControl(Control):
    pass

class LinuxControl(Control):
    pass

class MacOSControl(Control):
    pass

#фабрика для создания контролов на Windows
#каждая фабрика имеет методы для создания разных типов контроллов
class WindowsFactory:
    def createForm(self):
        return WindowsControl()

    def createLabel(self):
        return WindowsControl()

    def createTextBox(self):
        return WindowsControl()

    def createComboBox(self):
        return WindowsControl()

    def createButton(self):
        return WindowsControl()

#фабрика для создания контролов на Linux
class LinuxFactory:
    def createForm(self):
        return LinuxControl()

    def createLabel(self):
        return LinuxControl()

    def createTextBox(self):
        return LinuxControl()

    def createComboBox(self):
        return LinuxControl()

    def createButton(self):
        return LinuxControl()

#фабрика для создания контролов на MacOS
class MacOSFactory:
    def createForm(self):
        return MacOSControl()

    def createLabel(self):
        return MacOSControl()

    def createTextBox(self):
        return MacOSControl()

    def createComboBox(self):
        return MacOSControl()

    def createButton(self):
        return MacOSControl()

# Создание окна
root = tk.Tk()
root.title("Application")

# Список для выбора ос
os_label = tk.Label(root, text="Выберите операционную систему:")
os_label.pack()

os_combobox = ttk.Combobox(root, values=["Windows", "Linux", "Macos"])
os_combobox.pack()

# Список для выбора метода контролла
method_label = tk.Label(root, text="Выберите метод контролла:")
method_label.pack()

method_combobox = ttk.Combobox(root, values=[
    "setPosition",
    "getPosition",
    "OnValueChanged",
    "getSelectedIndex",
    "setSelectedIndex",
    "setItems",
    "getItems",
    "Click",
    "setText",
    "getText",
    "addControl"
])
method_combobox.pack()

# Функция для кнопки
def button_click():
    # Создание контролов
    os = os_combobox.get()
    os_factory = None
    if os == "Windows":
        os_factory = WindowsFactory()
    elif os == "Linux":
        os_factory = LinuxFactory()
    elif os == "Macos":
        os_factory = MacOSFactory()

    if os_factory:
        form = os_factory.createForm()
        label = os_factory.createLabel()
        textbox = os_factory.createTextBox()
        combobox = os_factory.createComboBox()
        button = os_factory.createButton()

        # Выбор метода из выпадающего списка
        method_name = method_combobox.get()

        # Вызов выбранного метода у контролла
        if hasattr(label, method_name):
            method = getattr(label, method_name)
            if callable(method):
                print(f"Вызван метод {method_name} у контролла {type(label).__name__}")
            else:
                print(f"{method_name} не является методом у контролла {type(label).__name__}")
        else:
            print(f"Метод {method_name} не существует у контролла {type(label).__name__}")
    else:
        print(f"Фабрика для операционной системы {os} не найдена.")

button = tk.Button(root, text="Вызвать метод", command=button_click)
button.pack()
root.mainloop()