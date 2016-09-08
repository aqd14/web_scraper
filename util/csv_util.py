import csv

class CsvUtil(object):
    def write_world_cup_data_to_file(self, file_path, worldcup_edition_list):
        if not worldcup_edition_list:
            print 'World Cup list is empty!'
            return
        
        with open(file_path, 'wb') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_ALL)
            for worldcup_edition in worldcup_edition_list:
                data_to_write = [worldcup_edition.edition, worldcup_edition.team_number, worldcup_edition.match_played,
                                worldcup_edition.goal_scored, worldcup_edition.average_goal, worldcup_edition.average_attendance]
                csv_writer.writerow(data_to_write)
     
     
    def write_champions_league_data_to_file(self, file_path, champions_league_data):
        if not champions_league_data:
            print 'Champions League data is empty!'
            return
        
        with open(file_path, 'wb') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_ALL)
            for team_data in champions_league_data:
                data_to_write = [team_data.team_name,
                                team_data.goals_scored,
                                team_data.goals_against,
                                team_data.yellow_cards,
                                team_data.red_cards,
                                team_data.attempts_on_target,
                                team_data.attempts_off_target,
                                team_data.offsides,
                                team_data.corners,
                                team_data.fouls_committed,
                                team_data.possession_time,
                                team_data.possession_percent]
                                
                csv_writer.writerow(data_to_write)