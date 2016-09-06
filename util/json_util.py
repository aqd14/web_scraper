import json

class JsonUtil(object):
    def write_data_to_file(self, file_path, worldcup_edition_list):
        if not worldcup_edition_list:
            print 'World Cup list is empty!'
            return
        
        with open(file_path, 'wb') as json_file:
            for worldcup_edition in worldcup_edition_list:
                json.dump(worldcup_edition.__dict__, json_file)
