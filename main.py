from flask import Flask, render_template


app = Flask(__name__)

#to ease development
DEBUG = True

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', css='index', title='Welcome')


if __name__ == "__main__":
    app.run(debug=DEBUG)
