from flask import Flask
from app.views.appointment_available_times_view import bp as available_times_bp
from app.views.appointment_view import bp as appointment_bp
from app.views.manipulate_appointment_view import bp as manipulate_appointment_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(available_times_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(manipulate_appointment_bp)

    return app
