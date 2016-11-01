import os

print "start of script..."

os.system("cd /usr/share/rainbowcrack")
for i in range (0, 10):
        os.system("rtgen md5 loweralpha-numeric 6 6 %s 3500 100000 0" % i)
os.system("rtsort *.rt") 
hashFile= raw_input("Give path to hash.txt")
os.system("mv %s /usr/share/rainbowcrack/" % hashFile)

print "end of script..."
