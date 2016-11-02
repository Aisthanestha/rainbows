import os
#this essentialy automates a lab for offnetsec, mk rt for loweraplhpanum, sort and then take md5 of a string and crack.
print "start of script..."

os.system("cd /usr/share/rainbowcrack")
for i in range (0, 10):
        os.system("rtgen md5 loweralpha-numeric 6 6 %s 3500 100000 0" % i)
os.system("rtsort md5*.rt") 
while agaiN="1":
        mkHash= raw_input("string to be made into md5 hash:\n")
        os.system("echo -n %s | md5sum | cat >> hash.txt" % mkHash)
        os.system("cp hash.txt hash1.txt")
        os.system("sed -e 's/-//' hash1.txt > hash.txt")
        os.system("rm hash1.txt")
        agaiN= raw_input("another hash?y/n")
os.system("rcrack md5_*.rt -l ")



print "end of script..."
