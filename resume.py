"""
Generate pdf resume from markdown and css.
"""

import argparse
import codecs
import os
import pdfkit

from jinja2 import Environment, PackageLoader, Markup
from markdown2 import markdown
#from subprocess import call


def parse_args():
    parser = argparse.ArgumentParser(
        description='Generate pdf resume from markdown and css'
    )
    parser.add_argument(
        '--css',
        dest='css',
        default='src/css/default.css',
        help='specify the path of the CSS file'
    )
    parser.add_argument(
        '-m',
        '--markdown',
        dest='markdown',
        default='src/md/john-cadengo.md',
        help=('specify the path of the MARKDOWN file')
    )

    args = parser.parse_args()
    return args


def generate_markdown(mdfile):
    """
    Generate html from a markdown file at the specified path.
    """
    f = codecs.open(mdfile, encoding='utf-8')
    html = Markup(markdown(f.read()))
    f.close()

    return html


def create_template(content, css):
    """
    Plug the html content into the body of the template.
    """
    env = Environment(loader=PackageLoader('resume', '.'))
    template = env.get_template('src/base.html')

    return template.render(content=content, css=css)


def main():
    args = parse_args()
    content = generate_markdown(args.markdown)
    template = create_template(content, args.css)
    filename = os.path.basename(args.markdown)
    name = os.path.splitext(filename)[0]

    if not os.path.exists('build/html'):
        os.makedirs('build/html')

    html = 'build/html/{}.html'.format(name)
    f = codecs.open(html, 'w', encoding='utf-8')
    f.write(template)
    f.close()

    # Generate a png
    #if not os.path.exists('build/png'):
    #    os.makedirs('build/png')

    #call(['wkhtmltoimage', html,
    #      './build/png/{}.png'.format(name)])

    # Generate the pdf
    if not os.path.exists('build/pdf'):
        os.makedirs('build/pdf')

    options = {
        'margin-top': '0.0',
        'margin-right': '0.0',
        'margin-bottom': '0.0',
        'margin-left': '0.0',
        'page-size': 'Letter'
    }
    pdfkit.from_file(html, './build/pdf/{}.pdf'.format(name), options)


if __name__ == '__main__':
    main()
