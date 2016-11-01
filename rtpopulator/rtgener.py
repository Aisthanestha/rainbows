import os
# this will create a rainbow table that is alpha-numerica ABCD...1234... with a plaintext length min of 6 and max of 6 with table index from 0 to 10 so it will take a while to generate. 
print "start of script..."
os.system("cd /usr/share/rainbowcrack")
ls = os.system("ls")
print "this is current dir"
print ls 
print "this will take a while"
for i in range (0, 10):
        os.system("rtgen md5 alpha-numeric 6 6 %s 3500 100000 0" % i)
os.system("rtsort *.rt") #sorts all .rt files in /usr/share/rainbowcrack
print "end of script..."
