from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    # Allow overriding the port via the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    try:
        app.run(debug=True, port=port)
    except OSError as exc:
        # Port already in use — try the next port and inform the user
        alt_port = port + 1
        print(f"Port {port} in use: {exc}. Trying port {alt_port}.")
        app.run(debug=True, port=alt_port)