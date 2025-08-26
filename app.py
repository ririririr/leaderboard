from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'your-very-secret-key-12345'  # Change this to a random, secret value in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


import colorsys

# Helper: get color from green to red based on rank (0=green, 1=red, spectrum)
def rank_to_color(rank, total):
    if total <= 1:
        return '#00c853'  # Only one, make it green
    t = (rank - 1) / (total - 1)
    h = 0.33 * (1 - t)  # 0.33=green, 0=red
    r, g, b = colorsys.hsv_to_rgb(h, 0.85, 0.85)
    return '#{:02x}{:02x}{:02x}'.format(int(r*255), int(g*255), int(b*255))

app.jinja_env.globals.update(rank_to_color=rank_to_color)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    earnings = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'earnings': self.earnings}

@app.route('/')
def index():
    players = Player.query.order_by(Player.earnings.desc()).all()
    return render_template('index.html', players=players)

@app.route('/add', methods=['POST'])
def add_player():
    name = request.form['name']
    earnings = float(request.form['earnings'])
    new_player = Player(name=name, earnings=earnings)
    db.session.add(new_player)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/api/players')
def api_players():
    players = Player.query.order_by(Player.earnings.desc()).all()
    return jsonify([p.to_dict() for p in players])


# Delete player route
@app.route('/delete/<int:player_id>', methods=['POST'])
def delete_player(player_id):
    player = Player.query.get_or_404(player_id)
    db.session.delete(player)
    db.session.commit()
    flash(f"Deleted {player.name} from leaderboard.", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists('leaderboard.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
