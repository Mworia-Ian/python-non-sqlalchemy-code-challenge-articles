class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string")
        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed after initialization")
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        magazines = set()
        for article in self._articles:
            magazines.add(article.magazine)
        return list(magazines)

    def create_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        topics = set()
        for article in self._articles:
            topics.add(article.magazine.category)
        return list(topics)

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        authors = set()
        for article in self._articles:
            authors.add(article.author)
        return list(authors)

    def article_titles(self):
        titles = []
        for article in self._articles:
            titles.append(article.title)
        return titles

    def prolific_contributors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        prolific_authors = []
        for author, count in author_counts.items():
            if count > 2:
                prolific_authors.append(author)
        return prolific_authors

class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters")
        if hasattr(self, "_title"):
            raise AttributeError("Title cannot be changed after initialization")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an Author object")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be a Magazine object")
        self._magazine = value