from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home() -> str:
    return render_template('home.html')

@app.route("/converter")
def converter() -> str:
    return render_template('number_to_word.html')

@app.route("/square_root")
def squareroot() -> str:
    return render_template('pythagorean_theorem.html')

@app.route("/hypotenuse")
def hypotenuse() -> str:
    return render_template('square_root.html')

if __name__ == "__main__":
    app.run(debug=False)