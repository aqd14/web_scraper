from lxml import html
from model.worldcup_stats import WorldCupStats
import requests
from model.champions_league_stats import ChampionsLeagueStats

def extract_worldcup_data(row):
    class_list = ['text', 'tbl-goalavg', 'tbl-attendanceavg']
    cols = list(row)
    for index, col in enumerate(cols):
        found_text = False
        for class_name in class_list:
            elements = col.find_class(class_name)
            if elements:
                found_text = True
                text = elements[0].text_content()
                print text
                break
            
        # Init value
        if found_text is True: 
            if index == 0:  # Edition, has Trade Mark
                edition = text.encode('utf8')
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
    worldcup_edition = WorldCupStats(edition, team_number, match_played, goal_scored, average_goal, average_attendance)
    return worldcup_edition

def extract_champions_league_data(row):
    # Get column data
    cols = list(row)
    # Extract data for each attributes
    team_name           = cols[0].text_content().encode('utf8') # Some football clubs has unicode characters 
    goals_scored        = cols[1].text_content()
    goals_against       = cols[2].text_content()
    yellow_cards        = cols[3].text_content()
    red_cards           = cols[4].text_content()
    attempts_on_target  = cols[5].text_content()
    attempts_off_target = cols[6].text_content()
    offsides            = cols[7].text_content()
    corners             = cols[8].text_content()
    fouls_committed     = cols[9].text_content()
    possession_time     = cols[10].text_content()
    possession_percent  = cols[11].text_content()
    
    for i in xrange(0, 11):
        print 'Row number: ' + str(i)
        print cols[i].text_content()
    team_data = ChampionsLeagueStats(team_name, goals_scored, goals_against, yellow_cards, red_cards,
                                     attempts_on_target, attempts_off_target, offsides,
                                     corners, fouls_committed, possession_time,possession_percent)
    return team_data
    
    
def get_row_data(url, table_class):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    # table = tree.xp
    table = tree.find_class(table_class)
    rows = table[0].xpath('.//tbody/tr')
#    rows = tree.xpath(row_xpath)
    return rows

class Scraper(object):
    def scrape_worldcup_data(self, url):
        """ Scrape World Cup data from url: http://www.fifa.com/fifa-tournaments/statistics-and-records/worldcup
        Try to get stats about 20 World Cup editions, including:
            1. Number of teams in each World Cup
            2. Matches
            3. Goals scored
            4. Average goals per match
            5. Average attendance per match
        """
        worldcup_edition_list = []
        rows = get_row_data(url, 'tbl-alleditions')
        for row in rows:
            worldcup_edition = extract_worldcup_data(row)
            # Initialize new Wolrd Cup object and add to list
            worldcup_edition_list.append(worldcup_edition)
        # Return list of world cup edition
        return worldcup_edition_list
    
    def scrape_champions_league_data(self, url):
        """ Scrape Champions League data from url: http://www.uefa.com/uefachampionsleague/season=2016/statistics/round=2000634/clubs/index.html
        Try to get stats of 32 European teams in tournament phase, including:
            1. Team name
            2. Number of goals scored
            3. Number of goals conceded
            4. Number of yellow cards
            5. Number of red cards
            6. Number of shoots on target
            7. Number of shoots off target
            8. Number of offsides
            9. Number of corners
            10. Number of fouls committed
            11. Number of ball possession in time
            12. Number of ball possession in percent
        """
        # List of team's data
        champions_league_team_data = []
        rows = get_row_data(url, 'clubstatoverview')
        for row in rows:
            team_data = extract_champions_league_data(row)
            champions_league_team_data.append(team_data)
        return champions_league_team_data