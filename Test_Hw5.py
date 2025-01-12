from datetime import time

def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    if time(hour=22) <= current_time <= time(hour=23):
        is_dark_theme = True
    elif time(hour=0) <= current_time <= time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    if dark_theme_enabled_by_user == True:
        is_dark_theme = True
    elif dark_theme_enabled_by_user == False:
        is_dark_theme = False
    else:
        if time(hour=22) <= current_time <= time(hour=23):
            is_dark_theme = True
        elif time(hour=0) <= current_time <= time(hour=6):
            is_dark_theme = True
        else:
            is_dark_theme = False

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"

    for user in users:
        if user['name'] == 'Olga':
            suitable_users = user

    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет

    suitable_users = []
    for user in users:
        if user['age'] < 20:
            suitable_users.append(user)
    print(suitable_users)

    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

def readble_print(func, arg):
    func_name = func.__name__.title().replace('_', ' ')
    arg_name = arg
    # print(func_name) #имя функции и аргументы
    # print(arg_name)
    return (f'{func_name} [{arg_name}]')  #имя функции и аргументы

def open_browser(browser_name):
    actual_result = readble_print(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"
    print(f'\n Ugly {open_browser.__name__}, {browser_name} \n Preaty {actual_result}')

def readble_CO(funcj, argj):
    name = funcj.__name__.title().replace('_', ' ')
    arg = argj
    return (f'{name} [{arg}]')

def go_to_companyname_homepage(page_url):
    actual_result = readble_CO(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"
    print(f'\n Ugly {go_to_companyname_homepage.__name__}, {page_url} \n Preaty {actual_result}')

def trololo(r, t, m):
    c = r.__name__.title().replace('_', ' ')
    a = t
    b = m
    return (f'{c} [{a}, {b}]')

def find_registration_button_on_login_page(page_url, button_text):
    actual_result = trololo(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
    print(f'\n Ugly {find_registration_button_on_login_page.__name__}, {page_url}, {button_text} \n Preaty {actual_result}')