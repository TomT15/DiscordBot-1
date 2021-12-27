import json

class filewriting:
    def writeToFile(Content):
        try:
            f = open("weaponTracker.txt", "a")
        except:
            f = open("weaponTracker.txt", "x")

        json_dump = json.dumps(Content)
        f.write()
        f.close()

        # open and read the file after the appending:
        f = open("weaponTracker.txt", "r")
        print(f.read())
