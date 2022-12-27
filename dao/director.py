from dao.model.director import Director


class DirectorDAO:
    """
    Класс работы с таблицей directors базы данных
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        Поиск одного значения в тадлице БД
        :param bid:
        :return:
        """
        return self.session.query(Director).get(bid)

    def get_all(self):
        """
        Выборка всех значений в таблице БД
        """
        return self.session.query(Director).all()

    def create(self, director_d):
        """
        Создание записи в таблице БД
        :param director_d:
        :return:
        """
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        Удаление записи таблицы БД
        :param rid:
        :return:
        """
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        """
        Обновление значений записи в таблице БД
        :param director_d:
        :return:
        """
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
