from control.scraper import Scraper
from util.csv_util import CsvUtil
from util.json_util import JsonUtil
import os

def main():
    url = 'http://www.fifa.com/fifa-tournaments/statistics-and-records/worldcup/'
    scraper = Scraper()
    worldcup_edition_list = scraper.scrape_worldcup_data(url)
    
    # Write data to file
    print 'Writing data to csv file!'
    cwd = os.getcwd()
    csv_writer = CsvUtil()
    csv_writer.write_data_to_file(cwd + os.sep + "data" + os.sep + 'world_cup_data.csv', worldcup_edition_list)
    
    print 'Writing data to json file!'
    json_writer = JsonUtil()
    json_writer.write_data_to_file(cwd + os.sep + "data" + os.sep + 'world_cup_data.json', worldcup_edition_list)
    
if __name__ == "__main__":
    print "Running main!"
    main()
    print "Finish!"