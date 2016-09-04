from lxml import html
import requests

from model.worldcup_editon import WorldCupEdition


def extract_data(row):
    cols = row.xpath('td')
    for index, col in enumerate(cols):
        text = col.xpath('.//text()')  
        if index == 0:
            edition = text
        elif index == 1:
            team_number = text
        elif index == 2:
            match_played = text
        elif index == 3:
            goal_scored = text
        elif index == 4:
            average_goal = text
        elif index == 5:
            average_attendance = text
        else:
            print "Wrong column number: " + str(index) + "!"
    worldcup_edition = WorldCupEdition(edition, team_number, match_played, goal_scored, average_goal, average_attendance)    
    return worldcup_edition


class Scraper(object):
    def scrape_worldcup_data(self, url):
        worldcup_edition_list = []
        page = requests.get(url)
        tree = html.fromstring(page.content)
        rows = tree.xpath('//*[@id="alleditions"]/div[2]/table/tbody/tr')
        for row in rows:
            worldcup_edition = extract_data(row)
            # Initialize new Wolrd Cup object and add to list
            worldcup_edition_list.append(worldcup_edition)
        # Return list of world cup edition
        return worldcup_edition_list