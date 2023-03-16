import os
import shutil


def main():
    url = str("https://open.spotify.com/album/4PyOq7kavqglGk3cexcygx")
    #url = str(input("Enter a URL: ")) 
    cmd = 'python -m spotdl ' + url
    print(cmd)
    os.system(cmd)
    filedestination = '/media/hdd/Music'
    mp3s = [f for f in os.listdir(filedestination) if f.endswith('.mp3')]
    one = mp3s[0]
    one = one.split('-', 1)[0]
    one = one.strip()

    if(os.path.exists(one) == False):
        os.mkdir(one)

    sourcepath = r'/media/hdd/Music'
    sourcefiles = os.listdir(sourcepath)
    destinationpath = r'/media/hdd/Music/'+ one
    for file in sourcefiles:
        if file.endswith('.mp3'):
            shutil.move(os.path.join(sourcepath,file), os.path.join(destinationpath,file))
main()
    
    
