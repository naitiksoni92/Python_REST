import flask
from flask import request, jsonify
import sqlite3
from colorthief import ColorThief

import base64
import os
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Wohooo!</h1><p>My python site is now live on localhost...</p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)
	
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
	
	
@app.route('/api/v1/getcolors', methods=['GET'])
def api_color():
    
    if 'imgurl' in request.args:
        imgurl = request.args['imgurl']
    
    if 'colorcount' in request.args:
        colorcount = int(request.args['colorcount'])
	

	#img_url = "https://picsum.photos/300"
    with open('pic1.jpg', 'wb') as handle:
        response = requests.get(imgurl, stream=True)


        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
			
			

    #color_thief = ColorThief('myImg.PNG')
    color_thief = ColorThief('pic1.jpg')

    if colorcount <= 3:
	    colorcount = 3
    # build a color palette
    palette = color_thief.get_palette(color_count=colorcount)
    #print(palette)


    if os.path.exists("pic1.jpg"):
        os.remove("pic1.jpg")


    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(palette)
	
	
@app.route('/api/v1/getcolorss', methods=['POST'])
def api_color_post():
    
    if 'imgurl' in request.json:
        imgurl = request.json['imgurl']
    
    if 'colorcount' in request.json:
        colorcount = int(request.json['colorcount'])
	

	#img_url = "https://picsum.photos/300"
    with open('pic1.jpg', 'wb') as handle:
        response = requests.get(imgurl, stream=True)


        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
			
			

    #color_thief = ColorThief('myImg.PNG')
    color_thief = ColorThief('pic1.jpg')

    if colorcount <= 3:
	    colorcount = 3
    # build a color palette
    palette = color_thief.get_palette(color_count=colorcount)
    #print(palette)


    if os.path.exists("pic1.jpg"):
        os.remove("pic1.jpg")


    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(palette)
	
	
app.run()
