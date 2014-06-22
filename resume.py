"""
Generate pdf resume from markdown and css.
"""

import codecs
import os
import pdfkit

from jinja2 import Environment, PackageLoader, Markup
from markdown2 import markdown
from optparse import OptionParser
from subprocess import call


def parse_options():
    usage = "%prog [options]"
    parser = OptionParser(usage=usage)
    parser.add_option(
        '--css',
        dest='css',
        default='src/css/default.css',
        help='specify the path of the LESS file used to generate the css'
    )
    parser.add_option(
        '-m',
        '--markdown',
        dest='markdown',
        default='src/md/john-cadengo.md',
        help=('specify the path of the MARKDOWN used to generate the content '
              'of the html')
    )

    (options, args) = parser.parse_args()
    return options


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
    options = parse_options()
    content = generate_markdown(options.markdown)
    template = create_template(content, options.css)

    if not os.path.exists('build/html'):
        os.makedirs('build/html')

    html = 'build/html/john-cadengo.html'
    f = codecs.open(html, 'w', encoding='utf-8')
    f.write(template)
    f.close()

    # Generate a png
    #if not os.path.exists('build/png'):
    #    os.makedirs('build/png')

    #call(['wkhtmltoimage', html,
    #      './build/png/john-cadengo.png'])

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
    pdfkit.from_file(html, './build/pdf/john-cadengo.pdf', options)


if __name__ == '__main__':
    main()
