import os

print "start of script..."

os.system("cd /usr/share/rainbowcrack")
for i in range (0, 10):
        os.system("rtgen md5 loweralpha-numeric 6 6 %s 3500 100000 0" % i)
os.system("rtsort *.rt") 
mkHash= raw_input("string to be made into md5 hash")
os.system("echo -n %s | md5sum " % mkHash)

print "end of script..."
