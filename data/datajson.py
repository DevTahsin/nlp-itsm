# reads b.json and store as a list of string array
import json2html

import json
# list directories
from os import listdir
from os.path import isfile, join

# list of files in the directory

def get_data(filename):
    with open('data/'+filename) as f:
        data = json.load(f)
    return data

# write string array to a file as json
def write_data(filename, data):
    with open('data/'+filename, 'w') as f:
        json.dump(data, f)
    
    with open('data/'+filename) as f:
        ## json.loads from file
        infoFromJson = json.loads(f.read())
    html = json2html.json2html.convert(json = infoFromJson)
    with open('data/'+filename+'.html', 'w') as f:
        f.write(html)
    