from flask import Flask, render_tempate


app = Flask(__name__)

#to ease development
DEBUG = True

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=DEBUG)
