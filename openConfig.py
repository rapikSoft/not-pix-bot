import json



def getConfig():
    with open("config.json" , "r") as f:
        

        config = json.loads(f.read())


        return config