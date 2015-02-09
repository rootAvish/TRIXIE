import shutil, os

def move(source, id3tags):
    # print id3tags
    #print "moving to " +  + "from " + source
    if (os.path.exists(source)):
        if 'ALBUM' in id3tags and 'ARTIST' in id3tags:
             
             s = id3tags['ARTIST'] + "\\"+ id3tags['ALBUM']
             dest = "".join(x for x in s if x.isalnum() or x == "\\" or x == " ")
             dest = movedir + dest
             if not os.path.isdir(dest):
                os.makedirs(dest)

             print dest
             if os.path.isdir(dest):
                try:
                    shutil.move(source, dest)
                except Exception, e:
                    return
             else:
                print "Could not create directories."

        else:
            print "skipping " + source + ", metadata not complete."


def destdir():
    global movedir
    movedir = raw_input('Enter directory where you want to move all your music to: ')

    if movedir[-1] != "\\":
        movedir += "\\"

    if not os.path.exists(movedir):
        os.makedirs(movedir)