import os
import json
from character import *

#def list_json_files():
#    json = []
#    for file in os.listdir():
#        if file.endswith('.json'):
#            json.append(file)
#    return json
#
#def print_saved_items():
#    for files in list_json_files():
#        print('___',files,'___')
#
#def save_new_item():
#    filename_in = input('Please name your file: ')
#    filename = open(filename_in + '.json' 'w')
#    json.dump(new_player.saved_dictionary(), filename)
#    filename.close()
#
#def load_saved_item():
#    filename_in = input('Please type the name of your file, without .json: ')
#    filename = open(filename_in + '.json' 'r')
#    loaded = json.load(filename)
#    new_player.name = loaded['name']
#    new_player.health = loaded['health']
#    new_player.max_healt = loaded['max-health']
#    new_player.dexterity = loaded['dexterity']
#    new_player.luck = loaded['luck']
#    new_player.max_luck = loaded['max-luck']
#    filename.close()
