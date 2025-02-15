from persistence_layer import UserDAO, PlaceDAO


class UserManager:
    def __init__(self):
        self.user_dao = UserDAO()

    def register_user(self, user_data):
        print("Registering user in Business Logic Layer")
        return self.user_dao.save(user_data)

    def update_user(self, user_id, user_data):
        print("Updating user in Business Logic Layer")
        return self.user_dao.update(user_id, user_data)

    def delete_user(self, user_id):
        print("Deleting user in Business Logic Layer")
        return self.user_dao.delete(user_id)


class PlaceManager:
    def __init__(self):
        self.place_dao = PlaceDAO()

    def create_place(self, place_data):
        print("Creating place in Business Logic Layer")
        return self.place_dao.save(place_data)

    def update_place(self, place_id, place_data):
        print("Updating place in Business Logic Layer")
        return self.place_dao.update(place_id, place_data)

    def delete_place(self, place_id):
        print("Deleting place in Business Logic Layer")
        return self.place_dao.delete(place_id)
