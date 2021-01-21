from app import db

class BookSubjectLink(db.Model):
    __tablename__ = 'book_subject_link'

    foreign_a = db.Column('foreign_a', db.Integer, db.ForeignKey('book.id'), primary_key = True)
    foreign_b = db.Column('foreign_b', db.Integer, db.ForeignKey('subject.id'), primary_key = True)

class BookAuthorLink(db.Model):
    __tablename__ = 'book_author_link'

    foreign_a = db.Column('foreign_a', db.Integer, db.ForeignKey('book.id'), primary_key = True)
    foreign_b = db.Column('foreign_b', db.Integer, db.ForeignKey('author.id'), primary_key = True)

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.String)
    printings = db.relationship('Printing')
    subjects = db.relationship('Subject', secondary = 'book_subject_link')
    websites = db.relationship('Website', secondary = 'printing')
    authors = db.relationship('Author', secondary = 'book_author_link')

    def __repr__(self):
        return f'<Book "{self.title}">'

class Printing(db.Model):
    __tablename__ = 'printing'

    id = db.Column('id', db.Integer, primary_key = True)
    book_id = db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
    city = db.Column('city', db.String)
    year = db.Column('year', db.Integer)
    website = db.Column('website', db.Integer, db.ForeignKey('website.id'))
    site = db.relationship('Website')
    url = db.Column('url', db.String)

class Website(db.Model):
    __tablename__ = 'website'

    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String)
    url = db.Column('url', db.String)
    count = db.Column('count', db.Integer)
    books = db.relationship('Book', secondary = 'printing')

    def __repr__(self):
        return f'<Website "{self.name}">'

class WebsiteUrl(db.Model):
    __tablename__ = 'website_url'

    id = db.Column('id', db.Integer, primary_key = True)
    site_id = db.Column('site_id', db.Integer, db.ForeignKey('website.id'))
    url = db.Column('url', db.String)

class Subject(db.Model):
    __tablename__ = 'subject'

    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String)
    count = db.Column('count', db.Integer)
    books = db.relationship('Book', secondary = 'book_subject_link')

    def __repr__(self):
        return f'<Subject "{self.name}">'

class Author(db.Model):
    __tablename__ = 'author'

    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String, unique=True)
    birth = db.Column('birth', db.Integer)
    death = db.Column('death', db.Integer)
    books = db.relationship('Book', secondary = 'book_author_link')

    def __repr__(self):
        return f'<Author "{self.name}">'