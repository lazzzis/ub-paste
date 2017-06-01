import os
import random
import webbrowser

import click
import requests
from requests.exceptions import ConnectionError

from ub_paste.language_map import language_map

USER_AGENTS = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
    ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
     'Chrome/19.0.1084.46 Safari/536.5'),
    ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
     'Safari/536.5'), )


@click.command()
@click.argument('filepath')
@click.option(
    '-a',
    '--author',
    default=os.getlogin(),
    help='The author name shown on ubuntu pastebin (defaults to your username)'
)
@click.option(
    '-n',
    '--no-browser',
    is_flag=True,
    help='Disallow script to open browser after pasting')
def cli(filepath, author, no_browser):
    '''This script reads a file and pastes the content to ubuntu pastebin'''
    extension = os.path.splitext(filepath)[1]
    syntax = language_map.get(extension, 'text')

    click.echo('reading...')

    with open(filepath, 'r') as f:
        content = f.read()

    click.echo('pasting...')

    try:
        r = requests.post(
            'http://pastebin.ubuntu.com',
            headers={'User-Agent': random.choice(USER_AGENTS)},
            data={'poster': author,
                  'syntax': syntax,
                  'content': content})
    except ConnectionError:
        click.echo(
            click.style(
                'Failed to establish network connection', fg='red'))
        return

    click.echo('Completed!')
    click.echo(click.style(r.url, fg='green'))

    if not no_browser:
        click.echo('opening browser...')
        webbrowser.open(r.url)
