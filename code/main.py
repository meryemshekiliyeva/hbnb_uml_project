from presentation_layer import ServiceAPI


def main():
    api = ServiceAPI()
    user_data = {"name": "Alice", "email": "alice@example.com"}
    user_id = api.register_user(user_data)
    print(f"Registered user with ID: {user_id}")

    place_data = {"title": "Sunny Villa", "price": 150}
    place_id = api.create_place(place_data)
    print(f"Created place with ID: {place_id}")

    updated_user_data = {"name": "Alice Smith", "email": "alice.smith@example.com"}
    api.update_user(user_id, updated_user_data)
  
    api.delete_place(place_id)


if __name__ == "__main__":
    main()
