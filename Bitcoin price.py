import requests

pre_result = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

result = pre_result.json()

print(f"USD: {result['bpi']['USD']['rate']} Dollar, Updated: {result ['time']['updated']} ")

print(f"GBP: {result['bpi']['GBP']['rate']} Pound, Updated: {result['time']['updated']}")

print(f"EUR: {result['bpi']['EUR']['rate']} Euro, Updated: {result['time']['updated']}")


     
print("\n")