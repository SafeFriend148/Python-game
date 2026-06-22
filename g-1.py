# состояние игры
inventory = set()
chest_opened = False
note_taken = False
PASSWORD = "1234"


# ===== ДЕЙСТВИЯ =====

def take_key():
    inventory.add("key")
    print("Вы подняли ключ.")

def open_chest():
    global chest_opened, note_taken
    if "key" in inventory:
        chest_opened = True
        note_taken = True
        inventory.add("note")
        print("Вы открыли сундук и нашли записку с паролем.")
    else:
        print("Сундук закрыт. Нужен ключ.")

def open_door():
    if "note" not in inventory:
        print("Дверь заперта. Нет записки с паролем.")
        return

    code = input("Введите пароль: ")
    check = lambda x: x == PASSWORD   # лямбда-функция

    if check(code):
        print("Дверь открыта. Вы выбрались!")
        exit()
    else:
        print("Неверный пароль.")

def show_inventory():
    print("Инвентарь:", inventory if inventory else "пусто")

def quit_game():
    print("Вы вышли из игры.")
    exit()


# ===== ФУНКЦИЯ ВЫСШЕГО ПОРЯДКА =====

def do_action(action):
    action()


# ===== КОМАНДЫ =====

actions = {
    "1": lambda: do_action(take_key),
    "2": lambda: do_action(open_chest),
    "3": lambda: do_action(open_door),
    "4": lambda: do_action(show_inventory),
    "0": lambda: do_action(quit_game)
}


# ===== ИГРОВОЙ ЦИКЛ =====

while True:
    print("""
1 — Поднять ключ
2 — Открыть сундук
3 — Открыть дверь
4 — Инвентарь
0 — Выход
""")

    choice = input("Выберите действие: ")
    actions.get(choice, lambda: print("Неверная команда"))()
