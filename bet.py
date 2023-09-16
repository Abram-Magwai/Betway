import argparse
import requests
from bs4 import BeautifulSoup

from pyfiglet import figlet_format 


logo = figlet_format("Bet", font = "isometric3" )

def fixtures(no_of_games = -1):
    url = 'https://www.betway.co.za/sport/soccer'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        games = soup.find_all(class_="league-group-event")
        size = len(games) if no_of_games is None else  int(no_of_games)
        for index in range(size):
            game = games[index]
            fixture = game.find('b').text

            date_and_time = game.find_all(class_="ellips")[1].text.replace('\n', ' ')
            outcomes = game.find_all(class_='outcome-pricedecimal')

            home_team_odds = "".join(outcomes[0].text.replace('\n', '').split())
            draw_odds = outcomes[1].text.replace('\n', '')
            away_team_odds = outcomes[2].text.replace('\n', '')
            print(f"{index+1}. => {fixture} => ({date_and_time}) => {home_team_odds} | {draw_odds} | {away_team_odds}")
    else:
        print('Failed to retrieve the web page.')

if __name__ == '__main__':
    print(f"{logo}\n")
    parser = argparse.ArgumentParser(description="Python script to get fixtures from betway (https://www.betway.co.za/sport/soccer)")
    parser.add_argument("-g", "--games", help="Number of games to list")

    args = parser.parse_args()
    no_of_games = args.games
    fixtures(no_of_games)
    