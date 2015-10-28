from flask import  Flask
from . import classifier

app = Flask(__name__)
app.register_blueprint(classifier.classifier, url_prefix='/classifier')
