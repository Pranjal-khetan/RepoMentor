
from flask import Flask, jsonify

# /Flask Application
app = Flask(__name__)


# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to RepoMentor!",
        "status": "Application is running"
    })


# Health check route
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
