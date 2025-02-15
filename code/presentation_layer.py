from business_logic_layer import UserManager, PlaceManager


class ServiceAPI:
    def __init__(self):
        self.user_manager = UserManager()
        self.place_manager = PlaceManager()

    def register_user(self, user_data):
        print("Registering user via Presentation Layer")
        return self.user_manager.register_user(user_data)

    def create_place(self, place_data):
        print("Creating place via Presentation Layer")
        return self.place_manager.create_place(place_data)

    def update_user(self, user_id, user_data):
        print("Updating user via Presentation Layer")
        return self.user_manager.update_user(user_id, user_data)

    def delete_place(self, place_id):
        print("Deleting place via Presentation Layer")
        return self.place_manager.delete_place(place_id)
