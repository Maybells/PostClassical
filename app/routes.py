from app import app
from app.models import Book, Author, Subject, Website
from app.forms import SearchForm
from flask import url_for, render_template, redirect, request


@app.route('/search/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == 'POST':
        print('Searched for: %s' % form.author.data)
        if form.author.data == '':
            form.author.data = None
        if form.subject.data == '':
            form.subject.data = None
        else:
            form.subject.data = form.subject.data.title()
        if form.website.data == '':
            form.website.data = None
        if form.title.data == '':
            form.title.data = None
        return redirect(url_for('view', title=form.title.data, author=form.author.data, website=form.website.data, subject=form.subject.data))
    
    subjects = Subject.query.order_by(Subject.name).all()
    #authors = Author.query.order_by(Author.name).all()
    websites = Website.query.order_by(Website.count.desc()).all()
    return render_template('search.html', form=form, subjects=subjects, websites=websites)

def match_args(input):
    args = ['author', 'website', 'subject']
    out = []
    for arg in args:
        if arg in input:
            out.append(arg)
    return out

@app.route('/view')
def view():
    args = request.args

    title = 'All Books'
    match = match_args(args)
    if len(match) == 0 and 'title' not in args:
        title = 'All Books'
    elif len(match) == 1:
        title = args[match[0]]
    else:
        title = 'Search'
    
    if 'page' in args:
        page = int(args['page'])
    else:
        page = 1
    vars = {}
    for arg in args:
        if arg != 'page':
            vars[arg] = args[arg]
    
    query = Book.query
    if 'title' in args and args['title'] != '':
        pattern = '%{}%'.format(args['title'])
        query = query.filter(Book.title.like(pattern))
    if 'author' in args and args['author'] != '':
        pattern = '%{}%'.format(args['author'])
        query = query.join(Book.authors).filter(Author.name.like(pattern))
    if 'website' in args and args['website'] != '':
        query = query.join(Book.websites).filter_by(name = args['website'])
    if 'subject' in args and args['subject'] != '':
        query = query.join(Book.subjects).filter_by(name = args['subject'])
    result = query.paginate(page=page, per_page=app.config['BOOKS_PER_PAGE'])

    return render_template('results.html', title = title, books = result, endpoint='view', vars=vars)

@app.route('/subjects/')
@app.route('/subjects/<int:page>')
def subjects(page=1):
    lst = Subject.query.order_by(Subject.count.desc()).paginate(page=page, per_page=app.config['CATEGORIES_PER_PAGE'])
    return render_template('subjects.html', subjects=lst, endpoint='subjects', vars=request.args)

@app.route('/sources/')
@app.route('/sources/<int:page>')
def websites(page=1):
    lst = Website.query.order_by(Website.count.desc()).paginate(page=page, per_page=app.config['CATEGORIES_PER_PAGE'])
    return render_template('websites.html', websites=lst, endpoint='websites', vars=request.args)

@app.route('/')
def home():
    return render_template('home.html', title='Post-Classical Library', book_count=Book.query.count())

@app.route('/contact/')
def contact():
    return render_template('contact.html', title='Under Construction')