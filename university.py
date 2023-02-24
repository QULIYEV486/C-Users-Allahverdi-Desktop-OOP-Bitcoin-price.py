import requests
universty = input()
pre_result = requests.get(f'http://universities.hipolabs.com/search?country={universty}')
result = pre_result.json()
for universty in result:
    print(f'Ad: {universty["name"]}')

    print(f'ölkə: {universty["country"]}')

     
    print("\n")







