class User(object):
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.address = address
        print (self.name + "'s email has been changed to: " + address)

    def __repr__(self):
        return("User: {username}, email: {email}, books read: {books_read}"\
        .format(username=self.name, email=self.email, books_read=len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return other_user == self
    '''
    extra methods requested in instructions
    '''
    def read_book(self, book, rating="None"):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        average = 0
        actual_review = 0
        for rating in self.books.values():
            if rating != None:
                total += rating
                actual_review += 1
        average = total / actual_review
        return round(average,1)

    '''
    Get Creative Methods
    '''
    def get_read_books(self):
        return len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn =  isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        return "{title}'s ISBN has been updated to: {isbn}"\
        .format(title=self.title, isbn=isbn)

    def add_rating(self, rating):
        self.rating = rating
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            return ("Invalid  Rating")
        return self.ratings

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return "This book already exists"

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_average_rating(self):
        total = 0
        average = 0
        for rating in self.ratings:
            total += rating
        average = total / len(self.ratings)
        return round(average,1)
    '''
    Get Creative Methods
    '''
    def __repr__(self):
        return self.title


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = str(author)

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = str(subject)
        self.level = str(level)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}"\
        .format(title=self.title, level=self.level, subject=self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            elif book not in self.books.keys():
                self.books[book] = 1
        else:
            print("No users with email {email}!".format(email=self.email))

    def add_user(self, name, email, user_books=None):
        if email not in self.users:
            self.users[email] = User(name, email)
            if user_books:
                for book in user_books:
                    self.add_book_to_user(book, email)
        else:
            print("User already exists")

    def print_catalog(self):
        for book in self.books.keys():
            print(book.title)

    def print_users(self):
        for user in self.users.values():
            print(user.name)

    def most_read_book(self):
        most_read_book = ""
        most_read = 0
        for book in self.books.keys():
            if self.books[book] > most_read:
                most_read = self.books[book]
            if self.books[book] == most_read:
                most_read_book = book
        return most_read_book

    def highest_rated_book(self):
        highest_rated = ""
        highest_rating = 0
        for book in self.books:
            average_rating = book.get_average_rating()
            if average_rating > highest_rating:
                highest_rating = average_rating
                highest_rated = book.title
        return highest_rated

    def most_positive_user(self):
        highest_average = 0
        highest_positive_user = ""
        for user in self.users.values():
            average_rating = user.get_average_rating()
            if average_rating > highest_average:
                highest_average = average_rating
                highest_positive_user = user.name
        return highest_positive_user
    '''
    Get Creative Methods
    '''
    def most_prolific_reader(self):
        books_read = 0
        prolific_reader = []
        for user in self.users.values():
            total_books = user.get_read_books()
            if total_books >= 5:
                books_read = total_books
                prolific_reader.append(user.name)
            if len(prolific_reader) == 0:
                prolific_reader.append("No one has made our top readers list yet... get reading!!!")
        return ' & '.join(prolific_reader)

    def __repr__(self):
        return "\tActive Users: {users}\n\tNumbers of books available: {books}\n\
        Most Popular Book: {popular}\n\tTop Readers: {readers}\
        ".format(users=len(self.users), books=len(self.books), popular=self.most_read_book(), readers=self.most_prolific_reader())
