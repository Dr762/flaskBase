# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from flask_send_mail import db
from flask_send_email import Role,User

#here we create sqlite db described in flsk_dbs. 
#Run this script to create db and load data 
#queries are also shown here
db.drop_all()
db.create_all()


admin_role= Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')

user_john = User(username='John',role=admin_role)
user_susan = User(username='Susan',role=user_role)
user_david = User(username='David',role=user_role)

db.session.add_all([admin_role,mod_role,user_role,
                    user_david,user_john,user_susan])

db.session.commit()

print Role.query.all()
print User.query.filter_by(role=user_role).all()
users = admin_role.users
print users
