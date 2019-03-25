Resume
======

A simple script to create a pdf version of my resume from markdown and css.

To create your own resume, [fork](https://github.com/johncadengo/Resume/fork) and edit the markdown file under `src/md`.

Outputs html and pdf to the `build` folder. Check out my [resume](https://github.com/johncadengo/Resume/raw/master/build/pdf/john-cadengo.pdf) below,

[![My resume](https://github.com/johncadengo/Resume/raw/master/build/pdf/john-cadengo.pdf)](https://github.com/johncadengo/Resume/raw/master/build/pdf/john-cadengo.pdf)

### Additional Requirements

Install `wkhtmltopdf` version 0.9.9. Any version after [hangs](http://stackoverflow.com/a/14043085) when run from the command-line.

Uninstall if you already have a later version,

    $ brew uninstall wkhtmltopdf

Install wkhtmltopdf version 0.9.9,

    $ brew install https://raw.github.com/mxcl/homebrew/6e2d550cf4961129a790bfb0973f8e88704f439d/Library/Formula/wkhtmltopdf.rb

### Usage

    $ python resume.py

### Roadmap

* Make into a web app with side by side markdown preview
* Add different css styles with options to interchange
