from flask import Flask ,url_for ,redirect ,render_template ,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/upload", methods=["POST","GET"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            return redirect(http://127.0.0.1:5000/uploaded)
    return render_template("upload_image.html")

@app.route("/uploaded")
def uploaded():
    return "Image uploaded"
if __name__ == "__main__":
    app.run(debug=True)