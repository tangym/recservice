from flask import Blueprint
from flask_restful import Api

from . import naive_bayes

classifier = Blueprint('classifier', __name__)
api = Api(classifier)

@classifier.route('/')
def index():
    # TODO: render document template
    return 'This should be the classifier model.\n'

@classifier.route('/<model>/doc')
def doc(model):
    # TODO: render document template
    return 'This should be the document of model %s\n' % model

# manipulate single resource 
api.add_resource(naive_bayes.NaiveBayesHandler, '/naive-bayes/<string:mid>')

# manipulate a group of resources
