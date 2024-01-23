from flask import Flask, request, render_template, flash
#from flask_debugtoolbar import DebugToolbarExtension
from data_search import find_part, material_flag, finishing_numbers, heat_treat_search, form_tool_search, fabricate, stamp, mirror_t_or_f, find_exception


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

#debug = DebugToolbarExtension


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route('/search_database_for_', methods=['GET', 'POST'])
def post_datat():
    part_number = request.form.get('part_id')
    part_data=find_part(part_number)
    if request.method == "POST" and part_data != None:
        flash(f"Found {part_number} in database", 'success')
        return render_template(
        "index.html",
        image_file= '/images' + "..images/abc.jpeg",
        part_num=part_number,
        part_data=part_data
        )
    else:
        flash(f"{part_number} was not found in database", 'failure')
        return render_template(
            "index.html",
             image_file= '/images' + "..images/abc.jpeg",
            part_num="",
            part_data=""
        )


@app.route('/gen_traveler_for', methods=['GET', 'POST'])
def gen_trav():
    part_number = request.form.get("part_id")
    part_data = find_part(part_number)
    if request.method == "POST" and part_data != None:
        flash(f"Generated traveler for {part_data}", 'success')
        return render_template(
            "trav.html",
            mirror =mirror_t_or_f(part_data.get("Mirror Part", "")),
            stock = part_data.get("Stock Size"),
            material = material_flag(part_number, part_data.get("Material")),
            fab = fabricate(part_data.get("Machined Part")),
            form = form_tool_search(part_data.get("Formed"), part_data.get("Tooling"), part_data.get("Mirror Part"), part_data.get("Mirror Part #"), part_number, part_data.get("Machined Part"), part_data.get("Part Name")),
            heat_treat = heat_treat_search(part_data.get("Finish"), find_exception(part_number)),
            mark = stamp(part_data.get("Part Mark"))
        )
    else:
        flash(f"Failed to generate traveler for {part_number}", 'failure')
        return render_template(
            "index.html"
        )
    
if __name__ == "__main__":
    app.run(debug=True)