import os
#this essentialy automates a lab for offnetsec, mk rt for loweraplhpanum, sort and then take md5 of a string and crack.
print "start of script..."

os.system("cd /usr/share/rainbowcrack")
tableS=int(raw_input("How many table indexes would you like?"))
for i in range (0, tableS):
        os.system("rtgen md5 loweralpha-numeric 6 6 %s 3500 100000 0" % i)

os.system("rtsort /usr/share/rainbowcrack/*.rt")

agaiN="y"

while agaiN =="y":
        mkHash= raw_input("string to be made into md5 hash:\n")
        os.system("echo -n %s | md5sum | cat >> /usr/share/rainbowcrack/hash.txt" % mkHash)
        os.system("cp /usr/share/rainbowcrack/hash.txt /usr/share/rainbowcrack/hash1.txt")
        os.system("sed -e 's/-//' /usr/share/rainbowcrack/hash1.txt > /usr/share/rainbowcrack/hash.txt")
        os.system("rm /usr/share/rainbowcrack/hash1.txt")
        agaiN= raw_input("another hash?y/n")

os.system("rcrack /usr/share/rainbowcrack/*.rt -l /usr/share/rainbowcrack/hash.txt")

print "end of script..."
