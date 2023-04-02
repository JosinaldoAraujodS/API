from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return "API IN THE AIR!"


@app.get("/ident/<name>")
def ident(name):
    return f"opa {name}"


if __name__ == "__main__":
    app.run(debug=True)

# att
