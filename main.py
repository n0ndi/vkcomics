import os
import requests
from random import randint
from dotenv import load_dotenv


def save_wall_photo(photo_server, photo_photo, photo_hash, access_token, group_id):
    params = {
        "server": photo_server,
        "photo": photo_photo,
        "hash": photo_hash,
        "access_token": access_token,
        "v": 5.131,
        "group_id": group_id
    }
    url = "https://api.vk.com/method/photos.saveWallPhoto"
    response = requests.post(url, params=params)
    return response.json()["response"][0]["id"]


def get_comics():
    url = "https://xkcd.com/info.0.json"
    filename = 'comics.jpg'
    response = requests.get(url)
    response.raise_for_status()
    current_comic_number = response.json()["num"]
    random_comic_number = randint(1, current_comic_number)
    random_comic_url = f"https://xkcd.com/{random_comic_number}/info.0.json"
    response = requests.get(random_comic_url)
    image = requests.get(response.json()["img"])
    with open(filename, 'wb') as file:
        file.write(image.content)
    return response.json()["alt"]


def get_upload_url(access_token, group_id, user_id):
    params = {
        "group_id": group_id,
        "access_token": access_token,
        "v": 5.131,
        "user_id": user_id
    }
    url = "https://api.vk.com/method/photos.getWallUploadServer"
    response = requests.get(url, params)
    return response.json()["response"]["upload_url"]
  

def send_photo_on_wall(upload_url):
    with open("comics.jpg", "rb") as file:
        response = requests.post(upload_url, files={"photo": file})
    params = response.json()
    return params["server"], params["photo"], params["hash"]


def post_image(group_id, media_id, access_token, message, user_id):
    url = "https://api.vk.com/method/wall.post"
    params = {
        "access_token": access_token,
        "owner_id": f"-{group_id}",
        "attachments": f"photo{user_id}_{media_id}",
        "message": message,
        "v": 5.131
    }

  
def main():
    load_dotenv()
    message = get_comics()
    vk_access_token = os.environ['VK_ACCESS_TOKEN']
    vk_group_id = os.environ['VK_GROUP_ID']
    vk_user_id = os.environ['VK_USER_ID']
    try:
        upload_url = get_upload_url(vk_access_token, vk_group_id, vk_user_id)
        photo_server, photo_photo, photo_hash = send_photo_on_wall(upload_url)
        media_id = save_wall_photo(photo_server, photo_photo, photo_hash, vk_access_token, vk_group_id)
        post_image(vk_group_id, media_id, vk_access_token, message, vk_user_id)
    finally:
        os.remove("comics.jpg")


if __name__ == "__main__":
    main()
