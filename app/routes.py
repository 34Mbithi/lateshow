from flask import Blueprint, jsonify, request
from .models import Episode, Guest, Appearance
from . import db

api_bp = Blueprint('api', __name__)

# get all episodes
@api_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": ep.id, "date": ep.date, "number": ep.number} for ep in episodes])

# get a specific episode by ID
@api_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode:
        appearances = [
            {
                "id": app.id,
                "rating": app.rating,
                "guest_id": app.guest_id,
                "guest": {
                    "id": app.guest.id,
                    "name": app.guest.name,
                    "occupation": app.guest.occupation
                }
            } for app in episode.appearances
        ]
        return jsonify({
            "id": episode.id,
            "date": episode.date,
            "number": episode.number,
            "appearances": appearances
        })
    else:
        return jsonify({"error": "Episode not found"}), 404

# get all guests
@api_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([{"id": guest.id, "name": guest.name, "occupation": guest.occupation} for guest in guests])

# create an appearance
@api_bp.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.get_json()
    try:
        appearance = Appearance(
            rating=data['rating'],
            episode_id=data['episode_id'],
            guest_id=data['guest_id']
        )
        db.session.add(appearance)
        db.session.commit()
        return jsonify({
            "id": appearance.id,
            "rating": appearance.rating,
            "guest_id": appearance.guest_id,
            "episode_id": appearance.episode_id,
            "episode": {
                "id": appearance.episode.id,
                "date": appearance.episode.date,
                "number": appearance.episode.number
            },
            "guest": {
                "id": appearance.guest.id,
                "name": appearance.guest.name,
                "occupation": appearance.guest.occupation
            }
        }), 201
    except Exception as e:
        return jsonify({"errors": ["validation errors"]}), 400

# delete an episode by ID
@api_bp.route('/episodes/<int:id>', methods=['DELETE'])
def delete_episode(id):
    episode = Episode.query.get(id)
    if episode:
        # Delete all appearances related to the episode
        db.session.delete(episode)
        db.session.commit()
        return jsonify({"message": f"Episode {id} deleted successfully"}), 200
    else:
        return jsonify({"error": "Episode not found"}), 404

