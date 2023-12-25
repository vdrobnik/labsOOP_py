import time
# 1) Создать виртуальную клавиатуру с переназначаемыми действиями для клавиш и комбинаций клавиш,
# с возможностью отката действий назад.
# 2) Продемонстрировать работу клавиатуры сделал WorkFlow из нажатий различных комбинаций клавиш и откатов назад.
# Симулировать демонстрацию нажатий клавиш путем вывода значения в консоль и задержкой между нажатиями
# 3) Продемонстрировать переназначение клавиши и комбинации клавиш с перезапуcком WorkFlow

# Погребной Владимир
# https://github.com/vdrobnik/labsOOP_py
# https://disk.yandex.ru/d/tCHxZ0RMunDLog

class Key:
    def __init__(self, keyName):
        self.keyName = keyName

    def getName(self):
        return self.keyName

    def setName(self, newKey):
        self.keyName = newKey

    def press_key(self, actions_obj):
        print(f'Нажата кнопка: {self.keyName}')
        time.sleep(1)
        actions_obj.addAction(self)

    def ExchangeName(self, newKeyName, actions_obj):
        print(f'Переобозначение: {self.keyName} -> {newKeyName}')
        for key in actions_obj.getActions():
            if key.getName() == self.keyName:
                key.setName(newKeyName)
        return actions_obj


class Actions:
    def __init__(self):
        self.actions = []

    def getActions(self):
        return self.actions

    def addAction(self, key):
        self.actions.append(key)

    def canselLastAction(self):
        if len(self.actions) > 0:
            last_action = self.actions.pop()
            print(f'Последние нажатие - {last_action.getName()}')
        else:
            print('Нет событий нажатия')

    def printActions(self):
        for iter in self.actions:
            print(iter.getName())


if __name__ == '__main__':
    actions_obj = Actions()
    key1 = Key('CTRL')
    key1.press_key(actions_obj)
    key2 = Key('SHIFT')
    key2.press_key(actions_obj)
    actions_obj.printActions()
    print('|||||||||||||||||||||||||||||||')
    # Откат последнего действия
    actions_obj.canselLastAction()
    actions_obj.printActions()
    print('|||||||||||||||||||||||||||||||')
    key2.press_key(actions_obj)
    actions_obj.printActions()
    print('|||||||||||||||||||||||||||||||')
    # Переназначение клавиш
    actions = key2.ExchangeName('Alt', actions_obj)
    actions_obj.printActions()
    print('|||||||||||||||||||||||||||||||')