from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
  return (
      "<h1>APSIT DevOps Lab - Assignment 1</h1>"
      "<p>CI/CD Pipeline with Jenkins, Docker, and GitHub is Running"
      " Successfully!</p>"
  )


@app.route("/health")
def health():
  return jsonify(status="healthy", code=200)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
