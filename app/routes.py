from flask import render_template, request, abort
from jinja2.exceptions import TemplateNotFound
from app import app


@app.route("/")
def index():
    return """<title>scripts - mahirchavda</title><style>.fun{font-family:cursive;font-style: italic;font-weight:bold;font-size:xx-large;}</style><center style="margin-top:47px;" class="fun">Hi, I'm mahirchavda</center>"""


@app.route("/<script_name>")
def get_script(script_name):
    try:
        return render_template(script_name, data=request.args, script_name=script_name)
    except TemplateNotFound as ex:
        abort(
            404,
            description='Unknown script: "{script_name}"'.format(
                script_name=script_name
            ),
        )
