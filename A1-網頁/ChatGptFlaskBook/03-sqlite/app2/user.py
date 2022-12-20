from flask import Blueprint, render_template, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@user_bp.route('/users/create', methods=['POST'])
def create_user():
    username = request.form.get('username')
    email = request.form.get('email')

    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()

    return 'User created successfully.'

@user_bp.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('user.html', user=user)

@user_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.username = request.form.get('username')
        user.email = request.form.get('email')
        db.session.commit()

        return 'User updated successfully.'
    else:
        return render_template('edit_user.html', user=user)

@user_bp.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return 'User deleted successfully.'
