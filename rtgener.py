import os
#this essentialy automates a lab for offnetsec, mk rt for loweraplhpanum, sort and then take md5 of a string and crack.
print "start of script..."

os.system("cd /usr/share/rainbowcrack")
wildCard = "*"
for i in range (0, 10):
        os.system("rtgen md5 loweralpha-numeric 6 6 %s 3500 100000 0" % i)
os.system("rtsort %s.rt" % wildCard ) 
mkHash= raw_input("string to be made into md5 hash")
os.system("echo -n %s | md5sum | cat >> hash.txt" % mkHash)
os.system("cp hash.txt hash1.txt")
os.system("sed -e 's/-//' hash1.txt > hash.txt")
os.system("rm hash1.txt")
os.system("rcrack %s.rt -l " % wildCard)



print "end of script..."
