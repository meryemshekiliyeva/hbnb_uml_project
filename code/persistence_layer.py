class UserDAO:
    def save(self, user_data):
        print(f"Saving user to database: {user_data}")
        return "user_id_123"

    def update(self, user_id, user_data):
        print(f"Updating user {user_id} in database: {user_data}")
    def delete(self, user_id):
        print(f"Deleting user {user_id} from database")
    def find(self, user_id):
        print(f"Finding user {user_id} in database")
        return {"id": user_id, "name": "John Doe"}


class PlaceDAO:
    def save(self, place_data):
        print(f"Saving place to database: {place_data}")
        return "place_id_456"

    def update(self, place_id, place_data):
        print(f"Updating place {place_id} in database: {place_data}")

    def delete(self, place_id):
        print(f"Deleting place {place_id} from database")

    def find(self, place_id):
        print(f"Finding place {place_id} in database")
        return {"id": place_id, "title": "Cozy Apartment"}
