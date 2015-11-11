from flask import render_template
from . import main

@main.app_errorhandler(404)
def page_not_found(e):
    print 'DBG : 404.html not found'
    return render_template('404.html'), 404

