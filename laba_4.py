import time
from typing import Dict


class Command:              # Поле num необходимо для того, чтобы при наследовании
    def execute(self, num): # можно было передавать значение клавиши/сочетания клавиш
        pass
    def undo(self, num):
        pass

class VirtualKeyboard(Command):
    def __init__(self):
        self._actions = []
        self._current_key = None
        self._volume = 50
        self.__key_actions = {
            'FN+F2': 'Volume down',
            'FN+F3': 'Volume up',
        }
    @property
    def actions(self):
        return self._actions
    @property
    def current_key(self):
        return self._current_key
    @property
    def volume(self):
        return self._volume
    @current_key.setter
    def current_key(self, key):
        self._current_key = key
    @current_key.deleter
    def current_key(self):
        del self._current_key

    # Переопределяем наследованные функции
    def execute(self, num):
        # self._actions.append(num)
        if num in self.__key_actions.keys(): # Смотрим есть ли в словаре наша команда
            action = self.__key_actions.get(num)
            self.volume_change(action.split()[-1])
            print(f"[INFO] Pressed {num} equal {action}")
        elif num.split()[0] == "Browser":# Browser open/close
            self.browser_change(num.split()[-1])
            print(f"[INFO] {num}")
        else:
            print(f"[INFO] Pressed button {num.split()[-1]}")

    def undo(self, last_action):
        deleted_history = self._actions[-1]
        self._actions.pop() # Удаляем последний элемент из списка действий
        print(f"Actions history: {self._actions}")
        split_last_action = last_action.split()[-1]
        if split_last_action == "FN+F2": # Отмена уменьшения громкости = увеличение громкости
            action = self.__key_actions.get("FN+F3")
            self.volume_change(action.split()[-1]) # Отправляем значение из словаря в функцию громкости
            print(f"[INFO] {split_last_action} and ctrl+z equal {action}")
        elif split_last_action == "FN+F3": # Отмена увеличения громкости = уменьшение громкости
            action = self.__key_actions.get("FN+F2")
            self.volume_change(action.split()[-1]) # Отправляем значение из словаря в функцию громкости
            print(f"[INFO] {split_last_action} and ctrl+z equal {action}")
        elif deleted_history.split()[1] == "Browser":
            if split_last_action == "open":
                self.browser_change('close')  # Browser open/close
                print(f"[INFO] After CTRL+Z: last action is pressed {self._actions[-1]}")
            elif split_last_action == 'close':
                self.browser_change('open')  # Browser open/close
                print(f"[INFO] After CTRL+Z: last action is pressed {self._actions[-1]}")
        else:
            print(f"[INFO] Cancel command-> Pressed {split_last_action}")
            print(f"[INFO] After CTRL+Z: last action is pressed {self._actions[-1]}")

    def volume_change(self, change, num=2):          # num - это насколько мы изменяем звук
         if change == 'up' and self._volume < 100:   # change - это в какую сторону меняем громкость
             self._volume +=num
             print(f"[INFO_VOLUME_CHANGER] volume UP: {self._volume}")
         elif change == 'down' and self._volume > 0:
             self._volume -=num
             print(f"[INFO_VOLUME_CHANGER] volume DOWN: {self._volume}")
         else:
             print("[INFO] Volume Changer Error-> Range limit")

    def browser_change(self, condition):
        if condition == "open":
            print("[INFO_BROWSER] Browser is opening")
        elif condition == 'close':
            print("[INFO_BROWSER] Browser is closing")

    def press_key(self, key):
        self._current_key = key
        action = f"Pressed {key}"
        print(action)
        if key in self.__key_actions:
            self._actions.append(action)
            self.execute(key)
        elif key == "ctrl+z":
            if len(self._actions) > 1:
                self.undo(self._actions[-1])
            else:
                print("[INFO] CTRL+Z cannot be used, the action's history is empty")
        else:
            self._actions.append(action)
            self.execute(key)

    def demonstrate_workflow(self):
        self.press_key('ctrl+z')
        self.press_key('A')
        self.press_key('alt')
        self.press_key('FN+F2')
        self.press_key("ctrl+z")
        self.press_key('FN+F3')
        self.press_key('C')

    def simulate_keystrokes(self):
        for key in "Hello,World!":
            self.press_key(key)
            time.sleep(0.5)

if __name__ == "__main__":
    keyboard = VirtualKeyboard()

    print("[Demonstrating Workflow]:")
    keyboard.demonstrate_workflow()

    print("\n[Simulating Keystrokes]:")
    keyboard.simulate_keystrokes()

    print("\nDemonstrating Browser and Workflow Restart:")
    keyboard.press_key('D')
    keyboard.press_key('Browser open')
    keyboard.press_key('ctrl+z')