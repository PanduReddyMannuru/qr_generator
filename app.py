from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_img = None

    if request.method == "POST":
        data = request.form["data"]

        qr = qrcode.make(data)

        if not os.path.exists("static"):
            os.mkdir("static")

        qr_path = "static/qr.png"
        qr.save(qr_path)

        qr_img = qr_path

    return render_template("index.html", qr_img=qr_img)

if __name__ == "__main__":
    app.run()
