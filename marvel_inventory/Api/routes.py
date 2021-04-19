from flask import Blueprint, request, jsonify
from marvel_inventory.helpers import token_required
from marvel_inventory.models import db,User,Character,character_schema, characters_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return { 'some': 'value'}


# CREATE character ENDPOINT
@api.route('/character', methods = ['POST'])
@token_required
def create_character(current_user_token):
    real_name = request.json['real_name']
    alias = request.json['alias']
    description = request.json['description']
    power = request.json['power']
    first_appearence = request.json['first_appearence']
    affliation = request.json['affliation']
    living_status= request.json['living_status']
    citizenship = request.json['citizenship']
    marital_status = request.json['marital_status']
    occupation = request.json['occupation']
    gender = request.json['gender']
    height = request.json['height']
    weight = request.json['weight']
    place_of_birth = request.json['place_of_birth']
    creators = request.json['creators']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    character = Character(real_name,alias,description,power,first_appearence,affliation,living_status,citizenship,marital_status,occupation,gender,height,weight,place_of_birth,creators,user_token = user_token )

    db.session.add(character)
    db.session.commit()

    response = character_schema.dump(character)
    return jsonify(response)




# RETRIEVE ALL  ENDPOINT
@api.route('/character', methods = ['GET'])
@token_required
def get_character(current_user_token):
    owner = current_user_token.token
    Character = character_schema.query.filter_by(user_token = owner).all()
    response = characters_schema.dump(Character)
    return jsonify(response)


# RETRIEVE ONE character ENDPOINT
@api.route('/character/<id>', methods = ['GET'])
@token_required
def get_drone(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        character = Character.query.get(id)
        response = character_schema.dump(character)
        return jsonify(response)
    else:
        return jsonify({"message": "Valid Token Required"}),401



# UPDATE charcater ENDPOINT
@api.route('/character/<id>', methods = ['POST','PUT'])
@token_required
def update_drone(current_user_token,id):
    character = Character.query.get(id) # GET DRONE INSTANCE
    character.real_name = request.json['real_name']
    character.alias = request.json['alias']
    character.description = request.json['description']
    character.power = request.json['power']
    character.first_appearence = request.json['first_appearence']
    character.affliation = request.json['affliation']
    character.living_status= request.json['living_status']
    character.citizenship = request.json['citizenship']
    character.marital_status = request.json['marital_status']
    character.occupation = request.json['occupation']
    character.gender = request.json['gender']
    character.height = request.json['height']
    character.weight = request.json['weight']
    character.place_of_birth = request.json['place_of_birth']
    character.creators = request.json['creators']
    character.user_token = current_user_token.token

    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)


# DELETE DRONE ENDPOINT
@api.route('/character/<id>', methods = ['DELETE'])
@token_required
def delete_character(current_user_token, id):
    character = Character.query.get(id)
    db.session.delete(character)
    db.session.commit()
    response = character_schema.dump(character)
    return jsonify(response)
