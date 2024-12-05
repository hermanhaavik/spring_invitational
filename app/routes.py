from flask import Blueprint, render_template, jsonify

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")

@main_bp.route("/api/leaderboard")
def leaderboard():
    data = [
        {"team": "Team Alpha", "points": 150},
        {"team": "Team Beta", "points": 120},
        {"team": "Team Gamma", "points": 100}
    ]
    return jsonify(data)
