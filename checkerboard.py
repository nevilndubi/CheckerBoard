from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home/<row>/<column>')
def checkerBoard(row, column):
    return render_template("index.html", rowNum=int(row), columnNum=int(column))


if __name__=="__main__":
    app.run(debug=True)