import json

MENU = '1) Добавить\n' \
       '2) Посмотреть\n' \
       '3) Выход\n-> '

tasks = []


def put_to_db(db_name):
    global tasks
    f = open(db_name, 'w')
    f.write(json.dumps(tasks))
    f.close()


def load_from_db(db_name):
    try:
        f = open(db_name)
    except FileNotFoundError:
        return []
    try:
        tasks = json.loads(f.read())
        f.close()
        return tasks
    except json.JSONDecodeError:
        return []


def add_item_to_db(item):
    global tasks
    if isinstance(item, str):
        tasks.append(item)
    else:
        print('Item not a str')


def get_items_from_db():
    global tasks
    return ', \n'.join(tasks)


def select_menu_item(choose_id):
    if choose_id == 1:
        item = input('Enter new item: ')
        add_item_to_db(item)
        print(f'{item} added successfully!')
    elif choose_id == 2:
        response = get_items_from_db()
        print(response)
    elif choose_id == 3:
        raise Exception('Exit')


def is_authorization(email, password):
    return email == 'admin@admin.com' and password == 'admin'


def main():
    email = input('email: ')
    password = input('password: ')
    if not is_authorization(email, password):
        print('Error')
        exit(0)
    while True:
        choose = input(MENU)
        if choose.isdigit() and int(choose) in [1, 2, 3]:
            select_menu_item(int(choose))
        else:
            print('ERROR')


if __name__ == '__main__':
    print('Hello User!')
    db_name = 'data.json'
    tasks = load_from_db(db_name)
    try:
        main()
    except Exception:
        put_to_db(db_name)
