import json



def getConfig():
    with open("config.json" , "r") as f:
        

        config = json.loads(f.read())


        return config
    

def getAccaunts(path,inps= None, g = True):

    print("\n\n\n")
    with open(path , "r") as f:

        arr = list(json.loads(f.read())["profile"]["info_cache"].items())


        if  inps == None:
            i = 0
            for profile in arr:
                print("--------------------------------------------------------------")
                i+=1;
                name =list(profile)[1]["name"]
                print(f"{i} : \"{list(profile)[0]}\" | Profile name: {name}")
                
                
            print("--------------------------------------------------------------")
            if g:
                while True:
                    try:
                        inp = int(input("\n\n\n🖌️ Please select profile to paint: "))-1
                        
                        return list(arr[inp])[0]
                        break
                    except:
                        print("❌ Please enter the correct number")
        else:
            profiles = []
            for inp in inps:
                profiles.append(list(arr[inp-1])[0])


            return profiles


if __name__ == "__main__":


    getAccaunts(getConfig()["chrome"]["pathToProfiles"]+"\\Local State",[1,2],g=False)