from flask import Flask, render_template
from backend import functions as comand
from flask_caching import Cache

app = Flask(__name__, template_folder='frontend/template', static_folder='frontend/static')

app.config.from_mapping({
    "CACHE_TYPE": "SimpleCache",  # caching type
    "CACHE_DEFAULT_TIMEOUT": 300 # default Cache Timeout
})

cache = Cache(app)

@app.route("/")
@cache.cached()
def homepage():
    comand.generateIndexHTML()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

