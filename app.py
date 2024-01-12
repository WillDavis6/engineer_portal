from flask import Flask, request, template 
from data_handler import find_part


app = Flask(__name__)

POST = {
    1: 'almuminum',
    2: 'steel',
    3: 'stainless steel',
    4: 'Titanium'
}

@app.route('/post/<int:id>')
def find_post(id):
    post = POST[id]
    return f'{post}'

@app.route('/find-part')
def get_part():
    return """
    <h1>search part data base</h1>
    <form method="POST">
        <input type="text" placeholder='part number' name='part-search'/>
        <button>Search Data Base</button>
    </form>
        """


search_number = request.form['part-search']
@app.route('/find-part', methods=['POST'])
def post_data():
    
    return  html_tempate(search_number)
