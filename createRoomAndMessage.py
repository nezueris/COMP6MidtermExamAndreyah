from webexteamssdk import WebexTeamsAPI

def get_access_token():
    choice = input("Do you want to use a hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
    else:
        access_token = "OTkxOWE4NWItNWRlYy00ZjJmLTg3MWUtMTgwZDk0NTM0Yzk4OTcyMmM0MjctMmYx_P0A1_d8874c41-f836-471b-bf45-f4bf285408d0"
    return access_token

def main():
    access_token = get_access_token()
    api = WebexTeamsAPI(access_token=access_token)

    # Create a room
    room_name = input("Enter the name of the room you want to create: ").strip()
    room = api.rooms.create(room_name)
    print(f"Room '{room.title}' created successfully with ID: {room.id}")

    # Send a welcome message
    welcome_message = input("Enter the welcome message you want to send: ").strip()
    api.messages.create(room.id, text=welcome_message)
    print("Welcome message sent successfully.")

if __name__ == "__main__":
    main()
