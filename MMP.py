import pygame 
from pygame import mixer
from mutagen.mp3 import MP3
import os
ruta = open('.path.txt', 'r')
path = ruta.read()
cc = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
playlist = []
playliststr = []
pygame.init()
mixer.init()

def mmp():

    cc()
    print("Minimalist Music Player\n")
    print("Select an Option:")
    print("1. Play a Song")
    print("2. Play a Playlist")
    print("3. Exit")
    op = input(">>>")

    if (op == "1"):
        
        music()
    if (op == "2"):
        
        mkplaylist()             
    if (op == "3"):
    
        print("Thanks for Use!")
        exit()
    else:
        mmp()
        
def music():
    
    try:
       song = input("\nSong: ")
       mixer.music.load(path + song)
       vol = input("Volume(0.0/1.0): ")
       volumen = float(vol)
       volstr = str(volumen)
       mixer.music.set_volume(volumen)
       num = input("Times a repeat the song(-1 is infinity): ")
       times = int(num)
       mixer.music.play(times)
    except:
        mixer.music.stop()
        print("Invalid values!")
        mmp()
        
    while True:
        
            volumen = float(vol)
            volstr = str(volumen)
            mixer.music.set_volume(volumen)
            audio = MP3(path + song)
            length = audio.info.length
            lengthmin = int(length/60)
            lengthsec = int(length%60)
            lengthstr = str(str(lengthmin) + ':' + str(lengthsec))
            cc()
            print("Song:" + song)
            print("Length:" + lengthstr)
            print("Volume:" + volstr)
            op = input(">>>")
    
            if (op == "q"):
        
                mixer.music.stop()
                mmp()
            if (op == "r"):
        
                mixer.music.play()
            if (op == "s"):
                
                try:
                   song = input("Song: ")
                   mixer.music.load(path + song)
                   mixer.music.play(times)
                except:
                    mixer.music.stop()
                    print("Your song don't exist")
                    return music()
                
            if (op == "v"):
                try:
                   vol = input("Volume(0.0/1.0): ")
                   volumen = float(vol)
                   volstr = str(volumen)
                   mixer.music.set_volume(volumen)
                except:
                    mixer.music.stop()
                    print("Invalid Value!")
                    return music()
                   
            if (op == "p"):
                mixer.music.pause()
            
            if (op == "unp"):
            
                mixer.music.unpause()
                
def mkplaylist():
    
    cc()
    print("1. Play the playlist")
    print("2. Add a song")
    print("3. Clear the playlist")
    op = input(">>> ")
    
    if op == "1":
        playplaylist()
    if op == "2":
        cc()
        song = input("Song: ")
        playlist.append(song)
        playliststr.append(song)
        mkplaylist()
    if op == "3":
        cc()
        playlist.clear()
        playliststr.clear()
        print("Playlist clear!")
        input("Press any key:")
        mkplaylist()
    else :
        mkplaylist()


def playplaylist():
    
    cc()
    try:
       mixer.music.load(path + playlist[0])
       playlist.pop(0)
       mixer.music.queue(path + playlist[0])
       playlist.pop(0)
       vol = input("Volume(0.0/1.0): ")
       volumen = float(vol)
       volstr = str(volumen)
       mixer.music.set_volume(volumen)
       num = input("Times a repeat a song(0 do not repeat): ")
       times = int(num)
       mixer.music.play(times)
    except:
        mixer.music.stop()
        print("Invalid values or songs in playlist!")
        mkplaylist()
        
    volumen = float(vol)
    volstr = str(volumen)
    mixer.music.set_volume(volumen)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    cc()
    print(f"Songs:{playliststr}")
    print("Volume:" + volstr)
    
    while True:
            
        for event in pygame.event.get():

            if event.type == pygame.USEREVENT:
                if len (playlist) > 0:
                    mixer.music.queue(path + playlist[0])
                    playlist.pop(0)
            if not pygame.mixer.music.get_busy():
                print("Playlist finished!")
                input("Press any key to return main menu:")
                mmp()
                    
if __name__ =="__main__":                
    mmp()
