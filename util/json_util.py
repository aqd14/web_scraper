import json

class JsonUtil(object):
    def write_world_cup_data_to_file(self, file_path, worldcup_edition_list):
        if not worldcup_edition_list:
            print 'World Cup list is empty!'
            return
        
        with open(file_path, 'wb') as json_file:
            for worldcup_edition in worldcup_edition_list:
                json.dump(worldcup_edition.__dict__, json_file)
                
    def write_champions_league_data_to_file(self, file_path, champions_league_data):
        if not champions_league_data:
            print 'Champions League data is empty!'
            return
        
        with open(file_path, 'wb') as json_file:
            for team_data in champions_league_data:
                json.dump(team_data.__dict__, json_file)