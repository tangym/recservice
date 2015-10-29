import os
import markdown
from flask import render_template, abort, Blueprint, Markup
from flask_restful import Api

from . import naive_bayes

BP_ROOT = os.path.dirname(os.path.abspath(__file__))
BP_STATIC = os.path.join(BP_ROOT, 'static')

classifier = Blueprint('classifier', __name__, template_folder=BP_ROOT)
api = Api(classifier)

@classifier.route('/')
def index():
    # TODO: render document template
    return 'This should be the classifier model.\n'

@classifier.route('/doc/<string:model>')
@classifier.route('/doc/<string:model>/')
def doc(model):
    # TODO: render document template
    try:
        with open(os.path.join(BP_STATIC, '%s.md' % model)) as file:
            content = file.read()
    except IOError:
        abort(404)
    else:
        content = Markup(markdown.markdown(content))
        return render_template('doc.template', model=model, doc=content)

# manipulate single resource 
api.add_resource(naive_bayes.NaiveBayesHandler, '/naive_bayes/<string:mid>')

# manipulate a group of resources
