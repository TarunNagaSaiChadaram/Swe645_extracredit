# Done By:
# - Samanvitha Matta (G01252738)
# - Akshaya Reddy Dundigalla (G01482843)
# - Tarun Naga Sai Chadaram (G01445928)
# A Flask application that uses RESTful APIs to manage Student Survey CRUD operations
# Establishes a connection to a configured database and makes create, read, update, and delete endpoints available.

# Demo Done

from flask import Flask, request, jsonify
from database import db
from models import StudentSurvey
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Routes
    @app.route('/surveys', methods=['GET'])
    def get_surveys():
        surveys = StudentSurvey.query.all()
        return jsonify([s.to_dict() for s in surveys])

    @app.route('/surveys/<int:survey_id>', methods=['GET'])
    def get_survey(survey_id):
        survey = StudentSurvey.query.get_or_404(survey_id)
        return jsonify(survey.to_dict())

    @app.route('/surveys', methods=['POST'])
    def create_survey():
        data = request.get_json()

        try:
            new_survey = StudentSurvey(
                first_name=data['first_name'],
                last_name=data['last_name'],
                street_address=data['street_address'],
                city=data['city'],
                state=data['state'],
                zip_code=data['zip_code'],
                phone=data['phone'],
                email=data['email'],
                campus_likes=data.get('campus_likes'),
                campus_interests=data.get('campus_interests'),
                recommend=data['recommend']
            )
            db.session.add(new_survey)
            db.session.commit()
            return jsonify(new_survey.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @app.route('/surveys/<int:survey_id>', methods=['PUT'])
    def update_survey(survey_id):
        survey = StudentSurvey.query.get_or_404(survey_id)
        data = request.get_json()

        try:
            survey.first_name = data['first_name']
            survey.last_name = data['last_name']
            survey.street_address = data['street_address']
            survey.city = data['city']
            survey.state = data['state']
            survey.zip_code = data['zip_code']
            survey.phone = data['phone']
            survey.email = data['email']
            survey.campus_likes = data.get('campus_likes')
            survey.campus_interests = data.get('campus_interests')
            survey.recommend = data['recommend']

            db.session.commit()
            return jsonify(survey.to_dict())
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    @app.route('/surveys/<int:survey_id>', methods=['DELETE'])
    def delete_survey(survey_id):
        survey = StudentSurvey.query.get_or_404(survey_id)
        try:
            db.session.delete(survey)
            db.session.commit()
            return jsonify({"message": "Survey deleted successfully."})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 400

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5001)
