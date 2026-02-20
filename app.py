from flask import Flask, render_template

app = Flask(__name__)

# Dummy threat data
def get_threat_data():
    return {
        "Threat": ["Malware", "Phishing", "Ransomware", "Zero-Day", "Botnet"],
        "Count": [50, 70, 40, 10, 25]
    }

@app.route("/")
def index():
    data = get_threat_data()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

