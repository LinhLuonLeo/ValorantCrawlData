import requests
from bs4 import BeautifulSoup
import csv

region = ("global", "na", "eu", "ap", "kr", "br", "latam")

for region in region:
    output_data = []
    output_data.append(("Rank", "Player", "Rank Rating", "Tier", "Wins"))
    for i in range(1, 2):
        url = f"https://tracker.gg/valorant/leaderboards/ranked/all/default?page={i}&region={region}"
        reponse = requests.get(url)
        soup = BeautifulSoup(reponse.content, "html.parser")
        table = soup.find("table", class_="trn-table")
        row = table.find_all("tr")
        for row in row:
                column = row.find_all("td")
                if column:
                    if int(column[0].text.strip())<=50:
                        rank = column[0].text.strip()
                        name = column[1].text.strip()
                        name = name.replace(" ","")
                        rank_rating = column[3].text.strip()
                        tier = column[4].text.strip()
                        wins = column[5].text.strip()
                        output_data.append((rank, name, rank_rating, tier, wins))
    with open(f"Data\\{region}Leaderboard.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(output_data)
    
        