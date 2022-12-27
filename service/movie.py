from dao.movie import MovieDAO


class MovieService:
    """
    Сервис для обработки операци над таблицей movie
    """
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        """
        Функция получения одной записи
        :param bid:
        :return:
        """
        return self.dao.get_one(bid)

    def get_all(self, filters):
        """
        Функция получения всех записей
        :param filters:
        :return:
        """
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_d):
        """
        Функция создания записи
        :param movie_d:
        :return:
        """
        return self.dao.create(movie_d)

    def update(self, movie_d):
        """
        Функция обновления данных записи
        :param movie_d:
        :return:
        """
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        """
        Функция удаления записи
        :param rid:
        :return:
        """
        self.dao.delete(rid)
