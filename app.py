from flask import Flask, request
from data_handler import find_part


app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return "no time for the wicked"

@app.route('/find-part')
def get_part():
    return """
    <h1>search part data base</h1>
    <form method="POST">
        <input type="text" placeholder='part number' name='part-search'/>
        <button>Search Data Base</button>
    </form>
        """

@app.route('/find-part')
def post_data():
    return  f"<h1>search part data base</h1>\n\
    <form method='POST'>\n\
    <input type='text' placeholder='part number' name='part-search'/>\n\
        <button>Search Data Base</button>\n\
    </form>\n\
    <p>{find_part(search_number)}"