from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<title>BNSP</title>
<h1>Ujian BNSP</h1>
<p>Semoga saya lulus</p>
<p>yang diperlukan adalah: Docker + AWS EC2 + CI/CD + Prometheus + Grafana</p>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
