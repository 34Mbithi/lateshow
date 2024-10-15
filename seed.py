from app import db, create_app
from app.models import Episode, Guest, Appearance

# Create an instance of the app
app = create_app()

def seed_data():
    with app.app_context():
        # Seed Episodes
        episodes = [
            {"date": "2024-01-01", "number": 1},
            {"date": "2024-01-02", "number": 2},
            {"date": "2024-01-03", "number": 3}
        ]
        
        for ep in episodes:
            episode = Episode(date=ep['date'], number=ep['number'])
            db.session.add(episode)
        
        # Seed Guests
        guests = [
            {"name": "John Doe", "occupation": "Actor"},
            {"name": "Jane Smith", "occupation": "Scientist"},
            {"name": "Alice Johnson", "occupation": "Musician"}
        ]
        
        for guest_data in guests:
            guest = Guest(name=guest_data['name'], occupation=guest_data['occupation'])
            db.session.add(guest)

        db.session.commit()

        # Seed Appearances
        appearances = [
            {"rating": 5, "episode_id": 1, "guest_id": 1},
            {"rating": 4, "episode_id": 2, "guest_id": 2},
            {"rating": 3, "episode_id": 3, "guest_id": 3},
            {"rating": 2, "episode_id": 1, "guest_id": 2},
            {"rating": 4, "episode_id": 2, "guest_id": 3},
        ]
        
        for app_data in appearances:
            appearance = Appearance(rating=app_data['rating'], episode_id=app_data['episode_id'], guest_id=app_data['guest_id'])
            db.session.add(appearance)

        db.session.commit()

if __name__ == '__main__':
    seed_data()
