def auth_required(login_status):
    def decorator(func):
        def check(user):
            if not isinstance(user, dict) or user.get('login_status') != login_status:
                user_name = user.get('name', 'ноунейм')
                raise PermissionError(f'Доступ запрещен, так как пользователь {user_name} не авторизовался')
            return func(user)

        return check

    return decorator


@auth_required(True)
def site_page(user):
    user_name = user.get('name', 'ноунейм')
    print(f'Пользователь {user_name} авторизовался и смог зайти на сайт')


user1 = {"name": "Валера", "login_status": True}
user2 = {"name": "Боря", "login_status": False}
site_page(user1)
site_page(user2)
