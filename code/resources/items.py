from flask import render_template, make_response
from flask_restful import Resource,Api,reqparse
from database import mycol,mycols



class Index(Resource):
    def get(self):
        headers={'Content-Type':'text/html'}
        data= mycol.find()
        items=[]

        for name in data:
              items.append(name)

        return make_response(render_template('index.html',name=items),200,headers)
        


class Details(Resource):
    def get(self):
        headers={'Content-Type':'text/html'}
        return make_response(render_template('details.html'),200,headers)
    
    def post(self):
        parse=reqparse.RequestParser()
        parse.add_argument('barcode',
        type=str,
        required=True
        )
        data=parse.parse_args()
        
        datas=mycols.find({"_ids":data['barcode']})
        headers={'Content-Type':'text/html'}
        if datas:
            for y in datas: 
                return make_response(render_template('displayItems.html',name=y),200,headers)
        
        return make_response(render_template('404.html'),200,headers)

