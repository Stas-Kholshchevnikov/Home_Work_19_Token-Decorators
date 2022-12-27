from dao.director import DirectorDAO


class DirectorService:
    """
    Сервис для обработки операци над таблицей directors
    """
    def __init__(self, dao: DirectorDAO):
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

    def create(self, director_d):
        """
        Функция создания записи
        :param director_d:
        :return:
        """
        return self.dao.create(director_d)

    def update(self, director_d):
        """
        Функция обновления данных записи
        :param director_d:
        :return:
        """
        self.dao.update(director_d)
        return self.dao

    def delete(self, rid):
        """
        Функция удаления записи
        :param rid:
        :return:
        """
        self.dao.delete(rid)