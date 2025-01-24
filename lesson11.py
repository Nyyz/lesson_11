class Data:
    def __init__(self):
        self.my_dict = {"key1": "value1", "key2": "value2"}
        self.my_tuple = (1, 2, 3)
    def login(self):
        a = input("як увійти?(user/admin)").strip().lower()
        if a == 'admin':
            b = input('введіть логін та пароль:').split()
            if b[0] == 'admin' and b[1] == '1234':
                print("hello admin")
                self.admin_menu()
            else:
                print("невірний логін або пароль")
        elif a == "user":
            print("Ви Юзер!")
            self.attribut()
    def attribut(self):
        print("Словник", self.my_dict)
        print("Кортеж", self.my_tuple)
    def admin_menu(self):
        while True:
            c = input('виберіть дію(словник/кортеж/вийти)')
            if c == "словник":
                self.go_dict()
            elif c == "кортеж":
                self.go_tuple()
            elif c == "вийти":
                break
            else:
                print("невірний вибір")
    def go_dict(self):
        diya1 = input("яку дію виконати?(додати/змінити/видалити/переглянути)")
        if diya1 == "додати":
            key = input("введіть ключ")
            value = input("введіть значення")
            if key in self.my_dict:
                goga = input("Ключ вже існує.Замінити значення?(так/ні):")
                if goga == "так":
                    self.my_dict[key] = value
            else:
                self.my_dict[key] = value
        elif diya1 == "замінити":
            key = input("введіть нове значення")
            if key in self.my_dict:
                value = input("введіть нове значення")
                self.my_dict[key] = value
            else:
                print("Значення не знайдено")
        elif diya1 == "видалити":
            delit = input("який елемент видалити")
            del self.my_dict[delit]
        elif diya1 == "переглянути":
            print(self.my_dict)
    def go_tuple(self):
        diya4 = input("яку дію виконати?(додати/переглянути)")
        if diya4 == "додати":
            diya5 = input("введіть елемент який бажаєте добавити:")
            self.my_tuple += (diya5)
        elif diya4 == "переглянути":
            print(self.my_tuple)
        else:
            print("Невірна дія")
if __name__ == "__main__":
    Run = Data()
    Run.login()


