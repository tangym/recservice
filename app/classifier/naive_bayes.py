from flask_restful import Resource

from . import base_model

class NaiveBayesHandler(Resource):
    def get(self, mid):
        # TODO: return model parameter
        return {'model': 'parameter'}
        
    def put(self, mid):
        # TODO: modify model parameter
        pass
    
    def  post(self, mid):
        # TODO: add a sample to train this model
        pass
    
    def delete(self, mid):
        # TODO: delete the model
        pass


class NaiveBayes(base_model.Classifier):
    pass

