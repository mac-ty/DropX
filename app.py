from flask import Flask, render_template, request
from utils import get_local_ip, generate_qr

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"


@app.route("/connect")
def connect_page():
    ip = get_local_ip()
    url = f"http://{ip}:5000"
    generate_qr(url, output_path="static/qr_code.png")
    return render_template("connect.html", url=url)



@app.route("/send")
def send_page():
    return render_template("send.html")


@app.route("/send-text", methods=["POST"])
def send_text():
    text = request.form.get("text", "").strip()
    if not text:
        return "No text received", 400
    print(f"[TEXT RECEIVED]: {text}")
    return "Text received!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
