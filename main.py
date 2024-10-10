import requests

from tqdm import tqdm

class VK:
    def __init__(self, access_token, user_id, owner_id, version = '5.131'):
        self.version = version
        self.owner_id = owner_id
        self.user_id = user_id
        self.base_url = 'https://api.vk.com/method/'
        self.access_token = access_token
        self.params = {
            'access_token':self.access_token,
            'v': self.version,
            'user_id': self.user_id,
            'owner_id': self.owner_id
        }

    def photos_get(self, album_id = 'profile', count = 1):
        url = f'{self.base_url}photos.get'
        params = {**self.params,
                  'album_id': album_id,
                  'extended': 1,
                  'photo_sizes': 1,
                  'count': count
                  }
        response = requests.get(url, params = params)
        images_dict = response.json()
        return images_dict

vk = VK(000000,333333333, 85858585)
photos = vk.photos_get()

def max_photos(photos):
    max_photo = {}
    for photo in photos['items']:
        for sizes in photo['sizes']:
            if sizes['type'] == 'z':
                max_photo[photo['id']] = {'user_likes': photo['user_likes'],
                                          'type': sizes['type'],
                                          'url': sizes['url'],
                                          'date': photo['date']
                                          }
            elif sizes['type'] == 'y':
                max_photo[photo['id']] = {'user_likes': photo['user_likes'],
                                          'type': sizes['type'],
                                          'url': sizes['url'],
                                          'date': photo['date']
                                          }
            return max_photo

images_url = max_photos(photos)
filename = images_url.get(f'{['user_likes']}_{['date']}')

res = requests.get(images_url)
with open(f'image/{filename}', 'wb') as f:
    f.write(res.content)

class YandexDisk:
    def __init__(self, token):
        self.headers = {
            'Autorizathion': f'OAuth {token}'
        }

        response = requests.put(url = 'https://cloud-api.yandex.net/v1/disk/resources',
                                headers = self.headers,
                                params = {'path':'Картинки с ВК'})

    def upload_folder(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {
            'path': f'Картинки с ВК/{filename}',
        }
        response = requests.get(upload_url,
                                params=params,
                                headers=self.headers)
        upload_link = res.json()['href']

        with open(f'image/{filename}', 'rb') as file:
            response = requests.put(upload_link, files={'file': file})

        for i in tqdm(range(100)):
            pass


yandex = YandexDisk(0000000)
yandex.upload_folder()



























