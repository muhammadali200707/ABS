# This file is Crud object
import json

from app.settings import generate_id
from model import User


def users_list():
    with open('db/users.json') as f:
        data = json.load(f)
    return data


def create_user(user: User):
    users = users_list()
    with open('db/users.json', 'w') as file:
        users[user.user_id] = user.__dict__
        json.dump(users, file, indent=3)
    print('User successfully created')


user = User(username='Anna', password='123321', user_id=generate_id())
# create_user(user)


# create_user(user)

def select_user(user_id: str):
    users = users_list()
    return users[user_id]


def update_user(user_id: str):
    users = users_list()
    for _id, user_value in users.items():
        if _id == user_id:
            user_value['username'] = input('Enter new username: ')
            user_value['email'] = input('Enter new email: ')
            with open('db/users.json', 'w') as file:
                json.dump(users, file, indent=3)
            return True
    return False


# update_user('1713590144120332300')


def delete_user(user_id: str):
    users = users_list()
    if user_id in users.keys():
        users.pop(user_id)
        with open('db/users.json', 'w') as file:
            json.dump(users, file, indent=3)
        return True
    return False


delete_user('1713590144120332300')
