
# 
# IMPORTS
# 
# you might have to import additional things you need

from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests

#
# SETUP/CONFIG
#
# change the classname to reflect the name of your table
# change the columns to reflect the columns you need
# each row of your data will be an instance of this class

app = Flask(__name__)

app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q8z\n\xec]/'

# change the following .db file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Anna-Levy.db'
# this line is to prevent SQLAlchemy from throwing a warning
# if you don't get one with out it, feel free to remove
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#
# DB SETUP
# 

# this set's up our db connection to our flask application
db = SQLAlchemy(app)

# this is our model (aka table)
class Bitcoin(db.Model):
    __tablename__ = "bitTable"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)
    Price = db.Column(db.String, nullable=False)
    _24h = db.Column(db.String, nullable=False)
    _7d = db.Column(db.String, nullable=False)
    Market_Cap = db.Column(db.String, nullable=False)
    Volume = db.Column(db.String, nullable=False)
    Circulating_Supply = db.Column(db.String, nullable=False)


@app.route('/api', methods=['GET'])
def get_data():
    table = Bitcoin.query.all()
    d = {row.id:[row.Name,row.Price,row._24h,row._7d,row.Market_Cap,row.Volume,row.Circulating_Supply] for row in table}
    return jsonify(d)

@app.route('/', methods=['GET'])
def welcome_message():
    return f"Hello and welcome to my Bitcoin Data from coinmarketcap.com website"





if __name__ == '__main__':
    app.run(debug=True)






#
# VIEWS 
#


# set up your index view to show your "home" page
# it should include:
# links to any pages you have
# information about your data
# information about how to access your data
# you can choose to output data on this page
# @app.route('/', methods=['GET'])
# def index():
#     data = Bitcoin.query.all()
#     return render_template('index.html', data=data)



# set up the following views to allow users to make
# GET requests to get your data in json
# POST requests to store/update some data
# DELETE requests to delete some data

# change this to return your data
# @app.route('/api', methods=['GET'])
# def get_data():tT†
#     table = Bitcoin.query.all()
#     d = {row.column_1:row.column_2 for row in table}
#     return jsonify(d)

# change this to allow users to add/update data
# @app.route('/api', methods=['POST'])
# def add_data():
#     if request.methodb == 'POST':
#         print(request.form)
#     for k,v in request.args.items():

#             #pass
#     return jsonify({})
        
# # change this to allow the deletion of data
# @app.route('/api', methods=['DELETE'])
# def delete_data():
#     for k,v in request.args.items():
#         pass
#     return jsonfiy({})

#
# CODE TO BE EXECUTED WHEN RAN AS SCRIPT
#


    
    
