from flask import Blueprint,render_template
from simpledu.models import Course,User

user=Blueprint('user',__name__,url_prefix='/user/admin')

@user.route('/')
def user_index():
	users=User.query.all()
	return render_template('user.html',users=users)