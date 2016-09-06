from lxml import html
from model.worldcup_editon import WorldCupEdition
import requests

def extract_data(row):
    class_list = ['text', 'tbl-goalavg', 'tbl-attendanceavg']
    cols = row.xpath('td')
    for index, col in enumerate(cols):
        for class_name in class_list:
            elements = col.find_class(class_name)
            if elements:
                text = elements[0].text_content()
                print text
                break
            
        # Init value 
        if index == 0:  # Edition, has TM
            edition = text.encode('ascii', 'ignore')
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