import requests


def price():

    URLS = ["https://api.coinmarketcap.com/v1/ticker/bitcoin","https://api.coinmarketcap.com/v1/ticker/ethereum/"]
    
    for URL in URLS :

        request = requests.get(URL)

        fjson = request.json()

        data = round (float(fjson[0]['price_usd']))

        name = fjson[0]['id']

        if name == "ethereum":

            print('1 ETH =',data,'$ ','\n')

        else:

            print('1 BTC =',data,'$','\n')

if __name__ == "__main__":

    price()






