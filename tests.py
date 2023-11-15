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
        assert len(collector.books_genre.keys()) == 2

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
        assert collector.books_genre[name] == genre

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
        assert collector.books_genre.get(name) is None

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        result = collector.get_book_genre('Гарри Поттер и философский камень')
        assert result == 'Фантастика'

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['Гарри Поттер и философский камень']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        result = collector.get_books_genre()
        assert result == {'Гарри Поттер и философский камень': 'Фантастика'}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        result = collector.get_books_for_children()
        assert result == ['Гарри Поттер и философский камень']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        assert 'Гарри Поттер и философский камень' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        collector.delete_book_from_favorites('Гарри Поттер и философский камень')
        assert 'Гарри Поттер и философский камень' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_book_in_favorites('Гарри Поттер и философский камень')
        assert 'Гарри Поттер и философский камень' in collector.get_list_of_favorites_books()