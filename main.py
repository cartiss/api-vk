import requests
from urllib.parse import urlencode, urljoin
from pprint import pprint

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

V = 5.124

class VKUser:
    def __init__(self, token, version, id):
        self.token = token
        self.version = version
        self.id = id

    def getFriend(self, user_id):
        FRIENDS_GET_URL = 'https://api.vk.com/method/friends.get'
        response = requests.get(FRIENDS_GET_URL, params={
            'user_id': user_id,
            'access_token': self.token,
            'v': self.version
        })
        return response.json()['response']['items']

    def getProfile(self):
        PROFILE_GET_URL = 'https://api.vk.com/method/users.get'
        response = requests.get(PROFILE_GET_URL, params={
            'access_token': self.token,
            'v': self.version,
            'user_id': self.id,
            'fields': ['screen_name']
        })
        result = response.json()['response'][0]['screen_name']
        return 'vk.com/' + result

    def __and__(self, other_user):
        friend_user1 = self.getFriend(self.id)
        friend_user2 = self.getFriend(other_user.id)
        pprint(set(friend_user1) | set(friend_user2))

    def __str__(self):
        return self.getProfile()

if __name__ == '__main__':
    user1 = VKUser(TOKEN, V, '----FIRST ID------')
    user2 = VKUser(TOKEN, V, '----SECOND ID-----')
    print(user2)