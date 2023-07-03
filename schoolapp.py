from flask import Flask
from blueprints.add_studentblueprint import student_blueprint
from blueprints.landingpageblueprint import landingPage_blueprint
from flask_mail import Mail
from config import Client
#--- Flask Setup --#
app = Flask(__name__)
app.register_blueprint(student_blueprint)
app.register_blueprint(landingPage_blueprint)

#--- Config controls ---#
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tejasjagannatha@gmail.com'
app.config['MAIL_PASSWORD'] = 'jvobkcyyfarnkmtq'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



if __name__ == '__main__':
    app.run(debug=True)

    # Close the MongoDB connection always outside the function
    Client.close()