# =========================
# 狀態管理器
# =========================
class StateManager:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, name, state):
        self.states[name] = state

    def change_state(self, name, **kwargs):
        if name not in self.states:
            print(f"State {name} 不存在")
            return

        if self.current_state:
            self.current_state.exit()

        self.current_state = self.states[name]
        self.current_state.enter(**kwargs)

    def handle_event(self, event_name):
        if self.current_state:
            self.current_state.handle_event(event_name)


# =========================
# 狀態基底類別
# =========================
class BaseState:
    def __init__(self, manager):
        self.manager = manager

    def enter(self, **kwargs):
        pass

    def exit(self):
        pass

    def handle_event(self, event_name):
        pass


# =========================
# 主選單狀態
# =========================
class MenuState(BaseState):
    def enter(self, **kwargs):
        print("進入 menu")

    def exit(self):
        print("離開 menu")

    def handle_event(self, event_name):
        if event_name == "BUTTON1":
            self.on_button1()

        elif event_name == "BUTTON2":
            self.on_button2()

        elif event_name == "BUTTON3":
            self.on_button3()

    def on_button1(self):
        self.manager.change_state("put_button1")

    def on_button2(self):
        self.manager.change_state("put_button2")

    def on_button3(self):
        self.manager.change_state("put_button3")


# =========================
# button1 狀態
# =========================
class PutButton1State(BaseState):
    def enter(self, **kwargs):
        print("進入 put_button1")
        self.do_action()

    def exit(self):
        print("離開 put_button1")

    def handle_event(self, event_name):
        if event_name == "BACK":
            self.on_back()

    def on_back(self):
        self.manager.change_state("menu")

    def do_action(self):
        print("執行 button1 的功能")
        # 這裡放 button1 對應的實際功能


# =========================
# button2 狀態
# =========================
class PutButton2State(BaseState):
    def enter(self, **kwargs):
        print("進入 put_button2")
        self.do_action()

    def exit(self):
        print("離開 put_button2")

    def handle_event(self, event_name):
        if event_name == "BACK":
            self.on_back()

    def on_back(self):
        self.manager.change_state("menu")

    def do_action(self):
        print("執行 button2 的功能")
        # 這裡放 button2 對應的實際功能


# =========================
# button3 狀態
# =========================
class PutButton3State(BaseState):
    def enter(self, **kwargs):
        print("進入 put_button3")
        self.do_action()

    def exit(self):
        print("離開 put_button3")

    def handle_event(self, event_name):
        if event_name == "BACK":
            self.on_back()

    def on_back(self):
        self.manager.change_state("menu")

    def do_action(self):
        print("執行 button3 的功能")
        # 這裡放 button3 對應的實際功能


# =========================
# 初始化狀態
# =========================
manager = StateManager()

manager.add_state("menu", MenuState(manager))
manager.add_state("put_button1", PutButton1State(manager))
manager.add_state("put_button2", PutButton2State(manager))
manager.add_state("put_button3", PutButton3State(manager))

manager.change_state("menu")


# =========================
# 事件判定函式
# 給 UI / pygame 組員呼叫
# =========================
def press_button1():
    manager.handle_event("BUTTON1")

def press_button2():
    manager.handle_event("BUTTON2")

def press_button3():
    manager.handle_event("BUTTON3")

def press_back():
    manager.handle_event("BACK")


# =========================
# 測試流程
# =========================
if __name__ == "__main__":
    press_button1()
    press_back()

    press_button2()
    press_back()

    press_button3()
    press_back()
