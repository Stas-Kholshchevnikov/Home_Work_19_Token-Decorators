from dao.model.genre import Genre


class GenreDAO:
    """
    Класс работы с таблицей genre базы данных
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        """
        Поиск одного значения в тадлице БД
        :param bid:
        :return:
        """
        return self.session.query(Genre).get(bid)

    def get_all(self):
        """
        Выборка всех значений в таблице БД
        :return:
        """
        return self.session.query(Genre).all()

    def create(self, genre_d):
        """
        Создание записи в таблице БД
        :param genre_d:
        :return:
        """
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        """
        Удаление записи таблицы БД
        :param rid:
        :return:
        """
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_d):
        """
        Обновление значений записи в таблице БД
        :param genre_d:
        :return:
        """
        genre = self.get_one(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self.session.add(genre)
        self.session.commit()
