import glob, colorama, json
from pygame import mixer

#setup stuff
mixer.init()
colorama.init(autoreset=True)

#loads settings

with open("./settings.json") as f:
    settings = json.loads(f.read())
mixer.music.set_volume(float(settings["volume"]))
loop = settings["loop"]


songs = glob.glob("./songs/*.*")#gets all songs in the songs folder


def play(cmd):
    if len(cmd.split(" ")) == 2:
        if not cmd.split(" ")[1] == "":
            song = int(cmd.split(" ")[1])-1
        else:
            return
    else:  
        for i in range(len(songs)):
            print(f"{i+1}: ", songs[i].removeprefix("./songs\\"))
        song = int(input())-1 

    if song <= len(songs):
        mixer.music.load(songs[song])
        mixer.music.play(99999999 if loop else 0)
    else:
        print("song does not exist")

def volume(cmd):
    newVolume = 100

    if len(cmd.split(" ")) == 2:
        newVolume = float(cmd.split(" ")[1])/100
        mixer.music.set_volume(newVolume)
    else:
        print(f"old volume: {round(mixer.music.get_volume()*100)}")
        newVolume = float(input("new volume: "))/100
        mixer.music.set_volume(newVolume)
    with open("settings.json", "r") as f:
        newSettings = json.loads(f.read())
    with open("settings.json", "w") as f:
        newSettings["volume"] = newVolume
        f.write(json.dumps(newSettings))

def commands():
    print(colorama.Fore.YELLOW + "play: opens a menu where you can select a song to play")
    print(colorama.Fore.YELLOW + "stop: stops the song")
    print(colorama.Fore.YELLOW + "pause: pauses the music")
    print(colorama.Fore.YELLOW + "unpause: unpauses the music")
    print(colorama.Fore.YELLOW + "volume: sets volume")
    print(colorama.Fore.GREEN + "help: opens the help menu")
    print(colorama.Fore.RED + "exit: exits the program")

print(f"\n{colorama.Fore.GREEN}type help if you need help")

while True:
    cmd = input(colorama.Fore.CYAN + "mjusikcs: " + colorama.Fore.RED).lower()
    print(end=colorama.Fore.RESET)

    match cmd.split(" ")[0]:
        case "play": play(cmd)
        case "pause": mixer.music.pause()
        case "unpause": mixer.music.unpause()
        case "exit": mixer.quit(), quit()
        case "stop": mixer.music.stop()
        case "help": commands()
        case "volume" | "vol": volume(cmd)

        case "": pass
        case _: print("command not found")