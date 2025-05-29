"""from os import system
system("cls")
"""

# import requests

# def get_api(url):
#     response = requests.get(url)

#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": f"Failed to fetch data, status code: {response.status_code}"}
    
# print(get_api("https://rickandmortyapi.com/api/character/1"))


# # {'characters': 'https://rickandmortyapi.com/api/character', 
# #  'locations': 'https://rickandmortyapi.com/api/location', 
# #  'episodes': 'https://rickandmortyapi.com/api/episode'}



"""

import requests

def get_api(url="https://rickandmortyapi.com/api"):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}
    
print(get_api())


# {'characters': 'https://rickandmortyapi.com/api/character', 
#  'locations': 'https://rickandmortyapi.com/api/location', 
#  'episodes': 'https://rickandmortyapi.com/api/episode'}

def get_object_from_characters(id=1):
    url = get_api().get("characters")
    response = requests.get(url + f"/{id}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch character with ID {id}, status code: {response.status_code}"}
    
print(get_object_from_characters(5))

def character_details(id=1):
    character = get_object_from_characters(id)
    if "error" in character:
        return character["error"]
    
    information = (
        f"Name: {character.get('name')}\n"
        f"Status: {character.get('status')}\n"
        f"Species: {character.get('species')}\n"
        f"Type: {character.get('type')}\n"
        f"Gender: {character.get('gender')}\n"
        f"Origin: {character.get('origin', {}).get('name')}\n"
        f"Location: {character.get('location', {}).get('name')}\n"
        f"Episode Count: {len(character.get('episode',[]))}\n"
    )
    return information

"""
# ### Задача: Реализация функций для получения и отображения информации о локациях из Rick and Morty API
# Необходимо реализовать две функции:
# ---
# #### 1. get_object_from_locations(id=1)
# Назначение:
# Получает объект локации по заданному ID из Rick and Morty API.
# Описание:
# * Использует базовый URL https://rickandmortyapi.com/api/location.
# * Выполняет HTTP-запрос к API по адресу https://rickandmortyapi.com/api/location/{id}.
# * Возвращает JSON-объект с данными о локации, если запрос успешен.
# * В случае ошибки возвращает словарь с ключом "error" и описанием ошибки.
# ---
# #### 2. location_detail(id=1)
# Назначение:
# Форматирует и возвращает читаемую информацию о локации.
# Описание:
# * Вызывает функцию get_object_from_locations.
# * Если в ответе есть ошибка, возвращает сообщение об ошибке.
# * Иначе возвращает строку с отформатированной информацией о локации, включая:
#   * Name — название локации;
#   * Type — тип (например, Planet, Space station);
#   * Dimension — измерение (например, Dimension C-137);
#   * Number of Residents — количество жителей (получается из длины списка residents).
# ---
# ### Пример вывода функции location_detail(1):
# Name: Earth (C-137)
# Type: Planet
# Dimension: Dimension C-137
# Number of Residents: 27

'''
from os import system
system("cls")
import requests

def get_api(url="https://rickandmortyapi.com/api"):
    response = requests.get(url)

    if response.status_code == 200:


        return response.json()
    else:
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}
    
print(get_api())




def get_object_from_locations(id=1):
    url = get_api().get("locations")
    response = requests.get(url + f"/{id}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch location with ID {id}, status code: {response.status_code}"}
    
print(get_object_from_locations(5))

def location_details(id=1):
    location = get_object_from_locations(id)
    if "error" in location:
        return location["error"]
    

    information = (
        f"Name: {location.get('name')}\n"
        f"Type: {location.get('type')}\n"
        f"Dimension.{location.get('dimension')}\n"
        f"Residents: {len(location.get('residents',[]))}\n"
    )
    return information
'''


from os import system
system("cls")
import requests

def get_api(url="https://rickandmortyapi.com/api"):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch data, status code: {response.status_code}"}
print(get_api())



def get_object_from_episodes(id=1):
    url = get_api().get("episodes")
    response = requests.get(url + f"/{id}")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch episode with ID {id}, status code: {response.status_code}"}
    
print(get_object_from_episodes(5))


def episode_details(id=1):
    episode = get_object_from_episodes(id)
    if "error" in episode:
        return episode["error"]

    information = (
        f"Name: {episode.get('name')}\n"
        f"Air date: {episode.get('air_date')}\n"
        f"Episode: {episode.get('episode')}\n"
        f"Characters: {len(episode.get('characters', []))}\n"
        f"Created: {episode.get('created')}\n"
    )
    return information


