import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre().keys()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize("name,genre", [
        ("Гордость и предубеждение и зомби", "Ужасы"),
        ("Что делать, если ваш кот хочет вас убить", "Комедии")
    ], ids=[
        "Possitive test 1",
        "Possitive test 2"
    ])
    def test_set_book_genre_set_genre_book_positive(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize("name, genre", [
        ("", "Фантастика"),
        ("", "")
    ], ids=[
        "Negative test with empty name",
        "Negative test with empty name, genre"
    ])
    def test_set_book_genre_set_genre_book_negative(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) is None

    @pytest.mark.parametrize("name, genre", [
        ("Гарри Поттер и философский камень", "Фантастика")
    ], ids=[
        "Positive test for get_book_genre"
    ])
    def test_get_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize("name, genre", [
        ("Гарри Поттер и философский камень", "Фантастика")
    ], ids=[
        "Positive test for get_books_with_specific_genre"
    ])
    def test_get_books_with_specific_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_books_with_specific_genre(genre)
        assert result == [name]

    @pytest.mark.parametrize("name, genre", [
        ("Гарри Поттер и философский камень", "Фантастика")
    ], ids=[
        "Positive test for get_book_genre"
    ])
    def test_get_books_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_books_genre()
        assert result == {name: genre}

    @pytest.mark.parametrize("name, genre", [
        ("Гарри Поттер и философский камень", "Фантастика")
    ], ids=[
        "Positive test for get_books_for_children"
    ])
    def test_get_books_for_children(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        result = collector.get_books_for_children()
        assert result == [name]

    @pytest.mark.parametrize("name, genre", [
        ("Гарри Поттер и философский камень", "Фантастика")
    ], ids=[
        "Positive test for add_book_in_favorites"
    ])
    def test_add_book_in_favorites(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("name, genre", [
        ("Гарри Поттер и философский камень", "Фантастика")
    ], ids=[
        "Positive test for delete_book_from_favorites"
    ])
    def test_delete_book_from_favorites(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("name, genre", [
        ("Гарри Поттер и философский камень", "Фантастика")
    ], ids=[
        "Positive test for get_list_of_favorites_books"
    ])
    def test_get_list_of_favorites_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()