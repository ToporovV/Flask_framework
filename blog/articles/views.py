from flask import Blueprint, render_template
from werkzeug.utils import redirect

article = Blueprint('articles', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        'title': 'Статья Александра',
        'text': 'Какой-то текст статьи Александра',
        'author': {
            'name': 'Александр',
            'id': 1,
        },
    },

    2: {
        'title': 'Статья Михаила',
        'text': 'Какой-то текст статьи Михаила',
        'author': {
            'name': 'Михаил',
            'id': 2,
        },
    },
    3: {
        'title': 'Статья Анастасии',
        'text': 'Какой-то текст статьи Анастасии',
        'author': {
            'name': 'Анастасия',
            'id': 3,
        },
    }
}


@article.route('/')
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@article.route('<int:id>')
def get_article(id: int):
    try:
        article = ARTICLES[id]
    except KeyError:
        return redirect('/articles/')
    return render_template(
        'articles/details.html',
        article=article,
    )


@article.route('<int:pk>')
def get_user(pk: int):
    try:
        user_name = ARTICLES[pk]['author']['name']
    except KeyError:
        return redirect('/users/')
    return render_template(
        'users/details.html',
        user_name=user_name,
    )
