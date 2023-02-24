import requests
film = input()
pre_result =  requests.get(f'https://imdb-api.com/API/Search/k_evw6tjj2/{film}')
result = pre_result.json()
films = result["results"]
for film in films:
    print(f'Ad: {film["title"]}')

    print(f'sekil: {film["image"]}')

    print(f'haqqinda: {film["description"]}')
    
    print("\n")


