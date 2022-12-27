from dao.model.user import User


class UserDAO:
    """
    ласс работы с таблицей user базы данных
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        """
        Поиск одного значения в тадлице БД
        :param uid:
        :return:
        """
        return self.session.query(User).get(uid)

    def get_all(self):
        """
        Выборка всех значений в таблице БД
        :return:
        """
        return self.session.query(User).all()

    def create(self, data):
        """
        Создание записи в таблице БД
        :param data:
        :return:
        """
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def update(self, data, uid):
        """
        Обновление значений записи в таблице БД
        :param data:
        :param uid:
        :return:
        """
        self.session.query(User).filter(User.id == uid).update(data)
        self.session.commit()
        return self.get_one(uid)

    def delete(self, uid):
        """
        Удаление записи таблицы БД
        :param uid:
        :return:
        """
        user = self.session.query(User).get(uid)
        self.session.delete(user)
        self.session.commit()
        return

    def get_by_name(self, user_name):
        """
        Выборка значения по совпадению имени пользователя
        :param user_name:
        :return:
        """
        return self.session.query(User).filter(User.username == user_name).one()

