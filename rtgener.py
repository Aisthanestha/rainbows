import os
#this essentialy automates a lab for offnetsec, mk rt for loweraplhpanum, sort and then take md5 of a string and crack.
print "start of script..."

os.system("cd /usr/share/rainbowcrack")
for i in range (0, 10):
        os.system("rtgen md5 loweralpha-numeric 6 6 %s 3500 100000 0" % i)
for x in range (0,10):
        os.system("rtsort md5_loweralpha-numeric#6-6_%s_3500x100000_0.rt" % x)

agaiN="y"

while agaiN =="y":
        mkHash= raw_input("string to be made into md5 hash:\n")
        os.system("echo -n %s | md5sum | cat >> hash.txt" % mkHash)
        os.system("cp hash.txt hash1.txt")
        os.system("sed -e 's/-//' hash1.txt > hash.txt")
        os.system("rm hash1.txt")
        agaiN= raw_input("another hash?y/n")

for z in range (0,10):
        os.system("rcrack md5_loweralpha-numeric#6-6_%s_3500x100000_0.rt -l hash.txt" % z)



print "end of script..."
