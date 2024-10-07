import requests

def get_access_token():
    choice = input("Do you want to use the hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
        access_token = "Bearer " + access_token
    else:
        access_token = "Bearer OTkxOWE4NWItNWRlYy00ZjJmLTg3MWUtMTgwZDk0NTM0Yzk4OTcyMmM0MjctMmYx_P0A1_d8874c41-f836-471b-bf45-f4bf285408d0"
    return access_token

def list_rooms(access_token):
    headers = {"Authorization": access_token}
    response = requests.get("https://webexapis.com/v1/rooms", headers=headers)

    if response.status_code != 200:
        print(f"Failed to retrieve rooms: {response.status_code} {response.text}")
        return []

    rooms = response.json().get("items", [])
    return rooms

def get_messages_in_room(access_token, room_id):
    headers = {"Authorization": access_token}
    params = {"roomId": room_id}
    response = requests.get("https://webexapis.com/v1/messages", headers=headers, params=params)

    if response.status_code != 200:
        print(f"Failed to retrieve messages: {response.status_code} {response.text}")
        return []

    messages = response.json().get("items", [])
    message_info = [(message["id"], message["text"]) for message in messages]
    return message_info

def delete_message(access_token, message_id):
    headers = {"Authorization": access_token}
    response = requests.delete(f"https://webexapis.com/v1/messages/{message_id}", headers=headers)

    if response.status_code == 204:
        print(f"Message {message_id} deleted successfully.")
    else:
        print(f"Failed to delete message {message_id}: {response.status_code} {response.text}")

def main():
    access_token = get_access_token()

    # List available rooms
    rooms = list_rooms(access_token)
    if not rooms:
        print("No rooms found.")
        return

    print("Available Rooms:")
    for room in rooms:
        print(f"Room ID: {room['id']}, Title: {room['title']}")

    # Allow user to select a room
    room_id = input("Enter the ID of the room you want to view messages from: ").strip()

    # Retrieve and print message IDs and text in the room
    message_info = get_messages_in_room(access_token, room_id)
    
    if not message_info:
        print("No messages found in the room.")
        return

    print("Messages in the room:")
    for message_id, text in message_info:
        print(f"Message ID: {message_id}, Text: {text}")

    # Allow user to choose which message to delete
    message_id_to_delete = input("Enter the ID of the message you want to delete: ").strip()
    
    # Check if the provided message ID exists
    if any(message_id == message_id_to_delete for message_id, _ in message_info):
        delete_message(access_token, message_id_to_delete)
    else:
        print("Invalid message ID. Please try again.")

if __name__ == "__main__":
    main()
