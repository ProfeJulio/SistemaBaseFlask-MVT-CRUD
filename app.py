from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index_base.html')


if __name__ == "__main__":
    # agregar el modo debugger
    app.run(debug=True)
