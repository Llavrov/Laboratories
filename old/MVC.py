
ManagerList = [
    {'name': 'Oleg', 'position': "senior"},
    {'name': 'Lev', 'position': "junior"},
    {'name': 'Ilya', 'position': "middle"}
]
Customer = [
    {'name': 'Andrey'},
    {'name': 'Dima'},
    {'name': 'Misha'}
]
Televisor = [
    {'model': 'dexp', 'price': 15000, 'quality': 8},
    {'model': 'sony', 'price': 35000, 'quality': 15},
    {'model': 'xiaomi', 'price': 36000, 'quality': 13},
]

items = list()  # global variable where we keep the data
people = list()  # global variable where we keep the data
customer = list()


class Equipment:
    def __init__(self, model, price, efficiency):
        self.model = model
        self.price = price
        self.efficiency = efficiency

    def get_Model(self):
        print(self.model)

    def get_Price(self):
        print(self.price)

    def get_efficiency(self):
        print(self.efficiency)


class Tv(Equipment):

    def specifications(self, model, price, efficiency, diag, ppi, resolution):
        Equipment.__init__(self, model, price, efficiency)
        self.diag = diag
        self.ppi = ppi
        self.resolution = resolution

    def get_diag(self):
        print(self.diag)

    def get_ppi(self):
        print(self.ppi)

    # Добавить лист с телевизорами
    def create_tele_list(self, app_items):
        global items
        items = app_items

    def read_names(self):
        global items
        lists = [item for item in items]
        result = []
        for i in range(len(lists)):
            result.append(lists[i]['model'])
        return result





class Notebook(Equipment):

    def __init__(self, model, price, efficiency, diag, battery_size, resolution):
        Equipment.__init__(self, model, price, efficiency)
        self.diag = diag
        self.battery_size = battery_size
        self.resolution = resolution

    def get_diag(self):
        print(self.diag)

    def get_battery_size(self):
        print(self.battery_size)


class Monitor(Equipment):

    def __init__(self, model, price, efficiency, diag, screen_type, resolution):
        Equipment.__init__(self, model, price, efficiency)
        self.diag = diag
        self.screen_type = screen_type
        self.resolution = resolution

    def get_diag(self):
        print(self.diag)

    def get_screen_type(self):
        print(self.screen_type)


class Printer(Equipment):

    def __init__(self, model, price, efficiency, speed, maximum_print_size, color_type):
        Equipment.__init__(self, model, price, efficiency)
        self.speed = speed
        self.maximum_print_size = maximum_print_size
        self.color_type = color_type

    def get_speed(self):
        print(self.speed)

    def get_color_type(self):
        print(self.color_type)


class Microwave(Equipment):

    def __init__(self, model, price, efficiency, capacity, defrost_function, container_size):
        Equipment.__init__(self, model, price, efficiency)
        self.capacity = capacity
        self.defrost_function = defrost_function
        self.container_size = container_size

    def get_Model(self):
        print(self.model)

    def get_container_size(self):
        print(self.container_size)



class Worker:

    def __init__(self, fullname, age, work_experience):
        self.fullname = fullname
        self.age = age
        self.work_experience = work_experience

    def get_name(self):
        print(self.fullname)

    def get_age(self):
        print(self.age)

    def get_work_experience(self):
        print(self.work_experience)


class Manager(Worker):

    def add_maneger(self, fullname, age, work_experience, sociability, appearance, charisma):
        Worker.__init__(self, fullname, age, work_experience)
        self.sociability = sociability
        self.appearance = appearance
        self.charisma = charisma

    def get_sociability(self):
        print(self.sociability)

    def get_charisma(self):
        print(self.charisma)

    # Добавим список менеджеров
    def create_Manager_list(self, app_items):
        global people
        people = app_items

    # Вывести список менеджеров
    def meneger_list(self):
        global people
        lists = [item for item in people]
        result = []
        for i in range(len(lists)):
            result.append(lists[i]['name'])
        return result


class Cashier(Worker):

    def __init__(self, fullname, age, work_experience, sociability, appearance, kindness):
        Worker.__init__(self, fullname, age, work_experience)
        self.sociability = sociability
        self.appearance = appearance
        self.kindness = kindness

    def get_sociability(self):
        print(self.sociability)

    def get_kindness(self):
        print(self.kindness)


# Класс покупателя, в котором будут инециализорованны функции
class Cust_buy:

    def __init__(self, name):
        self.name = name

    # Найти необходимый телевизор
    def find(self, model):
        self.model = model
        if read_item(model):
            print("we have one!")
            return True
        else:
            print("take another choise")

    # купить телевизор
    def buy(self, model):
        self.model = model
        if read_item(model):
            print("It's work!")
            buy_televisor(model)
        else:
            print("Sorry! We don't have that's one(")


class Customer(Cust_buy):
    def __init__(self, fullname):
        self.fullname = fullname

    # Добавим список покупателей
    def create_Customer_list(self, app_items):
        global customer
        customer = app_items

    def get_name(self):
        print(self.fullname)


# Создать новый лот
def create_item(model, price, quantity):
    global items
    items.append({'model': model, 'price': price, 'quality': quantity})


# Найти телевизор модели module
def read_item(model):
    global items
    myitems = list(filter(lambda x: x['model'] == model, items))
    if myitems:
        return myitems[0]
    else:
        print("oops!")


# Вывести список телевизоров
def read_items():
    global items
    return [item for item in items]



# Вывести список покупателей
def customer_list():
    global customer
    return [item for item in customer]


# Функция, которая будет убирать телефизор, который купили
def buy_televisor(model):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['model'] == model, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]

def choice_name(choice):
    new_model = input("Введите модель телевизора: ")
    Oleg.find(new_model)
    if read_item(new_model):
        ans = input("Хотите его преобрести? (Да/Нет): ")
        if ans == "Да":
            Oleg.buy("dexp")
            print("Поздравляю с покупкой! ")



# create_item("samsung", 15000, 15)



name = input("Введте имя пользователя: ")
Oleg = Customer(name)
tv = Tv(5, "dexp", 15000)
tv.create_tele_list(Televisor)
Ilya = Manager('Ivan', 24, 'strong')
Ilya.create_Manager_list(ManagerList)

yet = True
while yet:
    choice = int(input(name + ", вы можете выбрать модель телевизора, "
                   "который хотите купить, либо посмотреть список доступных телевизоров(1/2): "))
    if choice == 1:
        choice_name(choice)
    else:
        print(tv.read_names())
        choice = int(input(name + ", вы можете выбрать модель телевизора, "
                   "который хотите купить, либо обратиться к менеджеру и усточнить, насчет моделей (1/2): "))
        if choice == 1:
            choice_name(choice)
        else:
            print("К кому вы хотите обратиться ")
            print(Ilya.meneger_list())
            manager_name = int(input(' (1/2/3)?: '))

            if manager_name == 1:
                ask = input("Здравствуйте, " + name + ", меня зовут " + Ilya.meneger_list()[0] + ", что бы вы хотели узнать?: ")
            elif manager_name == 2:
                ask = input("Здравствуйте, " + name + ", меня зовут " + Ilya.meneger_list()[1] + ", что бы вы хотели узнать?: ")
            else:
                ask = input("Здравствуйте, " + name + ", меня зовут " + Ilya.meneger_list()[2] + ", что бы вы хотели узнать?: ")

            print("Хорошо, я уточню этот вопрос)")

    repeat = input("Вы уже уходите? (Да/Нет)? ")
    if repeat == "Да":
        print("Ничего, приходите в следующий раз)) ")
        print("Вот список наших менеджеров: ", Ilya.meneger_list())
        print("Список доступных телевизоров", tv.read_names())
        yet = False
    else:
        yet = True

