from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            result = eval(expression)
        except Exception as e:
            result = str(e)
        return render_template("index.html", expression=expression, result=result)
    return render_template("index.html", expression="", result="")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
