import paramiko
from scp import SCPClient
import os
import datetime
import sys

def main():
###############################################################
#   you need to pull files from /export/ftp1/ftp/pub on ftp   #
###############################################################

    
    now = datetime.datetime.now()

    filedir = "/export/threads/model/scud/" + str(now.year)
    fromMachine="ftp.soest.hawaii.edu"
    ssh = initSSH()

#    try:
 #       os.chdir(filedir)
  #  except:
   #     print("some error accessing directory (does it exist?")
    #    print("you tried:%s" % filedir)
     #   sys.exit()

    

    ftpCmd = ["ftp " + fromMachine, "prompt", "bin",
        "cd /hafner/SCUD/PACIOOS/" + str(now.year),
        "get " + str(now.year)+"-"+str(now.month)+"-"+str(now.day)+".nc", "quit"]

#    (stdin, stdout, stderr) = ssh.exec_command("pwd")
    
    fullStr=""




    for i in ftpCmd:
        fullStr += i
        fullStr += ";"

    print(fullStr)


    (stdin, stdout, stderr) = ssh.exec_command(fullStr)
    print(stderr.readlines())
         

    #for i in ftpCmd:


    


    
    #cmd = "ftp " + fromMachine + " << EOF"
    #ssh.exec_command(cmd)
    #cmd = 
    
    
    

    #cmd = 'cat ~/test.txt'

   

  



    scp = SCPClient(ssh.get_transport())
  #  scp.get("~/" + str(now.year)+"-"+str(now.month)+"-"+str(now.day)+".nc", str(now.year)+"-"+str(now.month)+"-"+str(now.day)+".nc")  
  #  scp.close()
    
    
    ssh.close()





def initSSH():

    ARCHIVE_SERVER = 'lawelawe.pacioos.hawaii.edu'

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 #  uncomment on prod
 #  ssh.connect(ARCHIVE_SERVER, username="owen", password="", key_filename='/home/owen/.ssh/id_rsa')
    ssh.connect(ARCHIVE_SERVER, username="owen", password="?SwclnX233")
    return ssh

if __name__ == "__main__":

    main()

