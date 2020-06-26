from flask import Flask
from flask_restful import Api

app=Flask(__name__)
api=Api(app)

from resources.items import Index
from resources.items import Details

api.add_resource(Index,'/')
api.add_resource(Details,'/details')

if __name__=='__main__':
   app.run(debug=True)