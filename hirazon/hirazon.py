import json
import requests

slack_token = 'xoxb-my-bot-token'
slack_channel = '#my-channel'
slack_icon_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuGqps7ZafuzUsViFGIremEL2a3NR0KO0s0RTCMXmzmREJd5m4MA&s'
slack_user_name = 'Alert'

def alert():
    print("Fahad")

    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_channel,
        'text': "Production and Dev core version are different",
        'icon_url': slack_icon_url,
        'username': slack_user_name,
    }).json()

def main():

    prod_version = requests.get('https://horizon.stellar.org/').json()["core_version"]
    dev_version = requests.get(' https://horizon-testnet.stellar.org/').json()["core_version"]

    if prod_version != dev_version:
        print("Not Equal")
        alert()


if __name__ == "__main__":
    main()