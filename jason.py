import json
from pathlib import Path 
defaults = {"theme": "dark", "language": "en", "font_size": 14}  

   

config_path= Path("config.json")

try :
    with open (config_path, "w", encoding="utf-8") as f :

        config = json.dump(defaults, f)
    print ("The file is loaded at the json")


except FileNotFoundError:


    config = defaults
    print ("Config file not found - used defaults")

except  json.JSONDecodeError as e :
    config = defaults
    print (f"the file is not the json {e}- used only defaults ")

print (config)
