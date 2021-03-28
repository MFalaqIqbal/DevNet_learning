import requests
import json
from pprint import pprint

personal_token = 'NTQxOWMxNDItMGQ0Yy00OTI5LWJjN2UtMDQ3YzkwMGEyYTc3MDc2MjQ3M2EtMDhj_PE93_a8b85d76-00ea-4bbe-a593-7087fa396e34'


def get_data(url, *args):
    if args == ():
        head = {
            "Authorization": f'Bearer {personal_token}',
            "Content-Type": "application/json"
        }
        res = requests.get(url=url, headers=head)
    else:
        head = {
            "Authorization": f'Bearer {personal_token}',
            "Content-Type": "application/json"
        }
        payload = args[0]
        res = requests.get(url=url, data=payload, headers=head)
    return res


def post_data(url, data):
    head = {
        "Authorization": f'Bearer {personal_token}',
        "Content-Type": "application/json"
    }
    res = requests.post(url=url, data=data, headers=head)
    return res


def create_teams(name):
    res = post_data(
            "https://webexapis.com/v1/teams",
            json.dumps(
                {
                    "name": f'{name}'
                }
            )
        )
    return res


def create_room(name, team_id):
    res = post_data(
            "https://webexapis.com/v1/rooms",
            json.dumps(
                {
                    'title': f'{name}',
                    'teamId': f'{team_id}'
                }
            )
        )
    return res


def get_all_messages(room_id):
    res = get_data(
        f'https://webexapis.com/v1/messages?roomId={room_id}'
    )
    return res


def post_message(room_id, text):
    res = post_data(
        "https://webexapis.com/v1/messages",
        json.dumps(
            {
                "roomId": f'{room_id}',
                "text":  f'{text}'
            }
        )
    )
    return res


def add_user(room_id, email, display_name, flag):
    res = post_data(
        "https://webexapis.com/v1/memberships",
        json.dumps(
            {
                'roomId': f'{room_id}',
                "personEmail": email,
                "personDisplayName": display_name,
                "isModerator": flag

            }
        )
    )
    return res


def main():
    """ This is a test sequence which
        1. creates a team,
        2. creates a room within that teams
        3. posts a message in room
        4. adds a user
    """
    create_teams("DevNet")
    get_all_team = get_data(f'https://webexapis.com/v1/teams')
    get_devnet_teams_id = get_all_team.json()['items'][0]['id']
    create_room("Room_1", get_devnet_teams_id)
    get_devnet_rooms = get_data(f'https://webexapis.com/v1/rooms?teamId={get_devnet_teams_id}')
    devnet_room_id = get_devnet_rooms.json()['items'][0]['id']
    post_message(devnet_room_id, "Hey it works")
    add_user(devnet_room_id, "test@gmail.com", "TEST_USER", "false")
    return


if __name__ == "__main__":
    main()
