from dao.genre import GenreDAO


class GenreService:
    """
    Сервис для обработки операци над таблицей genre
    """
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Функция получения одной записи
        :param bid:
        :return:
        """
        return self.dao.get_one(bid)

    def get_all(self):
        """
        Функция получения всех записей
        :return:
        """
        return self.dao.get_all()

    def create(self, genre_d):
        """
        Функция создания записи
        :param genre_d:
        :return:
        """
        return self.dao.create(genre_d)

    def update(self, genre_d):
        """
        Функция обновления данных записи
        :param genre_d:
        :return:
        """
        self.dao.update(genre_d)
        return self.dao

    def delete(self, rid):
        """
        Функция удаления записи
        :param rid:
        :return:
        """
        self.dao.delete(rid)
