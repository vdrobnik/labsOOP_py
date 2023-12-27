import time
# Не работает откат послднего действяи. не продемонстрирован вывод в консоль от клавиш, пчатающих текст

class Command:
    def execute(self):
        pass

class VirtualKeyboard(Command):
    def __init__(self):
        self._actions = []
        self._current_key = None

    @property
    def actions(self):
        return self._actions

    @property
    def current_key(self):
        return self._current_key

    @current_key.setter
    def current_key(self, key):
        self._current_key = key

    @current_key.deleter
    def current_key(self):
        del self._current_key

    def execute(self):
        pass

    def press_key(self, key):
        self.current_key = key
        action = f"Pressed {key}"
        self._actions.append(action)
        print(action)

    def reassign_key(self, key, new_action):
        if key in self._actions:
            original_action = f"Pressed {key}"
            index = self._actions.index(original_action)
            reassigned_action = f"Reassigned {key} to {new_action}"
            self._actions.insert(index + 1, reassigned_action)
            print(f"Key {key} reassigned to {new_action}")
        else:
            print(f"Key {key} not found in actions")

    def undo_last_action(self):
        if self._actions:
            undone_action = self._actions.pop()
            print(f"Undone action: {undone_action}")
            if self._actions:
                print(f"Last key pressed after rollback: {self._actions[-1].split()[-1]}")
            else:
                print("No actions remaining")
        else:
            print("No actions to undo")

    def demonstrate_workflow(self):
        self.press_key('A')
        self.press_key('B')
        self.undo_last_action()
        self.press_key('C')
        self.reassign_key('C', 'Print Hello')#переназначение С для печати приветствия
        self.press_key('C')
        self.undo_last_action()
        self.undo_last_action()

    def simulate_keystrokes(self):
        for key in "Hello, World!":
            self.press_key(key)
            time.sleep(0.5)

class Browser(VirtualKeyboard):
    def close_browser(self):
        self._actions.append("Closing the browser")
        print("Closing the browser")

    def open_browser(self):
        self._actions.append("Open the browser")
        print("Open the browser")

    def undo_last_action(self):
        if self.actions:
            undone_action = self.actions.pop()
            print(f"Undone action: {undone_action}")
            if "Pressed" in undone_action:
                print(f"Last key pressed after rollback: {self.actions[-1].split()[-1]}")
            elif "Closing the browser" in undone_action:
                print("Reopening the browser")
                self.actions.append("Reopened the browser")
            else:
                print("No actions remaining")
        else:
            print("No actions to undo")

if __name__ == "__main__":
    keyboard = Browser()

    print("Demonstrating Workflow:")
    keyboard.demonstrate_workflow()

    print("\nSimulating Keystrokes:")
    keyboard.simulate_keystrokes()

    print("\nDemonstrating Reassignment and Workflow Restart:")
    keyboard.press_key('D')
    keyboard.press_key('E')
    keyboard.undo_last_action()
    keyboard.undo_last_action()
    # keyboard.demonstrate_workflow()

    print("\nClosing and Reopening Browser:")
    keyboard.open_browser()
    keyboard.close_browser()
    keyboard.undo_last_action()