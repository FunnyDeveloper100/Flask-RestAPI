from flask_restful import Resource


class domain(Resource):
    def get(self):
        return 'domain list here'