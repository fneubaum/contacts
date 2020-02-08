from flask import jsonify, request, current_app
from models import ContactModel, contact_from_dict, db
from schemas import ContactSchema
from marshmallow import ValidationError
from app import app
from flask_sqlalchemy import SQLAlchemy


@app.route("/api/v1/contact", methods=['GET'])
def get_contacts():
    contacts = ContactModel.query.filter().all()
    schema = ContactSchema(many=True)
    result = schema.dump(contacts)
    return jsonify({'list': result})


@app.route("/api/v1/contact", methods=['POST'])
def post_contact():
    try:
        contact_dict = ContactSchema().load(request.json)
    except ValidationError as err:
        response = jsonify(err.messages)
        response.status_code = 400
        return response
    contact_model = ContactModel()
    new_contact = contact_from_dict(
        contact_dict, contact_model, is_creation=True)
    schema = ContactSchema()
    response = jsonify(schema.dump(new_contact))
    response.status_code = 202
    return response


@app.route("/api/v1/contact/<contact_id>", methods=['GET'])
def get_contact(contact_id):
    contact = ContactModel.query.filter_by(id=contact_id).first()
    if contact is None:
        response = jsonify({
            'message': 'contact does not exist'
        })
        response.status_code = 404
        return response
    schema = ContactSchema()
    result = schema.dump(contact)
    return jsonify(result)


@app.route("/api/v1/contact/<contact_id>", methods=['PUT'])
def put_contact(contact_id):
    schema = ContactSchema()
    try:
        contact_dict = schema.load(request.json)
    except ValidationError as err:
        response = jsonify(err.messages)
        response.status_code = 400
        return response
    contact = ContactModel.query.get(contact_id)
    if contact is None:
        response = jsonify({
            'message': 'contact does not exist'
        })
        response.status_code = 404
        return response
    modified = contact_from_dict(contact_dict, contact)
    schema = ContactSchema()
    response = jsonify(schema.dump(modified))
    response.status_code = 200
    return response


@app.route("/api/v1/contact/<contact_id>", methods=['DELETE'])
def delete_contact(contact_id):
    contact = ContactModel.query.get(contact_id)
    if contact is None:
        response = jsonify({
            'message': 'Contact does not exist'
        })
        response.status_code = 404
        return response
    db.session.delete(contact)
    db.session.commit()
    response = jsonify({
        'message': 'Contact deleted successfully'
    })
    response.status_code = 200
    return response

@app.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404

@app.after_request  # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    header['Access-Control-Request-Headers'] = '*'
    header['Access-Control-Allow-Methods'] = '*'
    return response
