from control.scraper import Scraper
from util.csv_util import CsvUtil
from util.json_util import JsonUtil
import os

def main():
    worldcup_url = 'http://www.fifa.com/fifa-tournaments/statistics-and-records/worldcup/'
    champions_league_url = 'http://www.uefa.com/uefachampionsleague/season=2016/statistics/round=2000634/clubs/index.html'
    
    scraper = Scraper()
    cwd = os.getcwd()
    csv_util = CsvUtil()
    json_util = JsonUtil()
    # Scrape World Cup data then write to csv and json format
    worldcup_edition_list = scraper.scrape_worldcup_data(worldcup_url)
     
    # Write data to file
    print 'Writing World Cup data to csv file!'
    csv_util.write_world_cup_data_to_file(cwd + os.sep + "data" + os.sep + 'world_cup_data.csv', worldcup_edition_list)
     
    print 'Writing World Cup data to json file!'
    json_util.write_world_cup_data_to_file(cwd + os.sep + "data" + os.sep + 'world_cup_data.json', worldcup_edition_list)
    
    # Scrape Champions League data then write to csv and json format
    champions_league_teams = scraper.scrape_champions_league_data(champions_league_url)
    # Write data to file
    print 'Writing Champions League data to csv file!'
    csv_util.write_champions_league_data_to_file(cwd + os.sep + "data" + os.sep + 'champions_league_data.csv', champions_league_teams)
    
    print 'Writing Champions League data to json file!'
    json_util.write_champions_league_data_to_file(cwd + os.sep + "data" + os.sep + 'champions_league_data.json', champions_league_teams)
    
if __name__ == "__main__":
    print "Running main!"
    main()
    print "Finish!"