import csv

class CsvUtil(object):
    def write_data_to_file(self, file_path, worldcup_edition_list):
        if not worldcup_edition_list:
            print 'World Cup list is empty!'
            return
        
        with open(file_path, 'wb') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_ALL)
            for worldcup_edition in worldcup_edition_list:
                data_to_write = [worldcup_edition.edition, worldcup_edition.team_number, worldcup_edition.match_played,
                                worldcup_edition.goal_scored, worldcup_edition.average_goal, worldcup_edition.average_attendance]
                csv_writer.writerow(data_to_write)
        