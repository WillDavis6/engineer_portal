from flask import Flask, request
from data_search import find_part

@app.route(f'/find-part/<part_number>', methods=['POST'])
def post_data(part_number):
    part_number = request.form['part-search']
    return  f"<h1>search part data base</h1>\n\
    <form method='POST'>\n\
    <input type='text' placeholder='part number' name='part-search'/>\n\
        <button>Search Data Base</button>\n\
    </form>\n\
    <p>{find_part(part_number)}"

