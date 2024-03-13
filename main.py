from instagrapi import Client
from instagrapi.types import Usertag, Location
import random
import config


class LikePost:
    def __init__(self, client):
        self.cl = client 
        self.tags = ['arduino'] # Список тегов по которым программа будет искать посты и лайкать их
        self.like_medias = [] # Список для проверки повторяющихся постов

    def get_post_id(self):
        medias = cl.hashtag_media_recent(random.choice(self.tags), amount = 1) # Поиск поста по одну из случайных тегов из списка
        media_dict = medias[0].dict()
        return str(media_dict['id'])
    
    def like_post(self, amount):
        for i in range(amount): 
            random_post = self.get_post_id()
            if random_post in self.like_medias: # Проверка для постов
                pass
            else:
                self.cl.media_like(media_id = random_post)
                self.like_medias.append(random_post)
                random_daley = random.randint(20, 60) #Случайная задержка между лайками
                time.sleep(random_daley)


class MadeContent:
    def __init__(self, client):
        self.cl = client 

    def made_post(self,image,text,users,post_location):
        self.cl.photo_upload(
            path = image, # Путь к картинке
            caption = text, # Описание поста 
            
            usertags = users ,# Отметака других пользователей на фото на вход подается 
                              # список пользовательей в формате:
                              # Usertag(user = имя пользователя, x = , y = )
                              # x и y точка отметки на фото
            location = post_location, # Добавить локацию где сделан пост
                                      # Формат Location(name = отображаемое имя, lat = , lng = )
                                      # lat и lng точка отметки на крате
            extra_data = {
                "like_and_views_counts_disabled": False, # отображение просмотров и лайков
                "disacled_comments": False # отображение коментарив
            })
    def made_photo_story(self,image):
        self.cl.photo_upload_to_story(image) 

    def made_video_story(self,video):
        self.cl.video_upload_to_story(video)

    def made_reals(self,video_path,text,thumbnail_path):
        self.cl.clip_upload(
            video_path, # путь к видео
            text, # Описание/текст под вашим рилсом
            thumbnail_path, # путь к превью

        )


cl = Client() # Создание пользователя 
cl.set_proxy(config.proxy) # Настройка прокси
cl.login(config.username, config.password) # Вход в систему для дальнейших действий
