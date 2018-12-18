#!/usr/bin/python3


from ftplib import FTP
import datetime
import os
import sys

def main():
    now = datetime.datetime.now()
    filedir = "/export/data/aco/adcp/" + str(now.year) + "/" + str(now.month)
    ftpHost="mananui.soest.hawaii.edu"
    ftp = initftp(ftpHost)

    try:
        os.chdir(filedir)
    except:
      print("some error accessing directory (does it exist?")
      print("you tried:%s" % filedir)
      #sys.exit()


    filename = str(now.year)+"-"+str(now.month)+"-"+str(now.day)+".nc"

    ftp.cwd("/hafner/SCUD/PACIOOS/" + str(now.year))

    with open(filename, "wb") as file: ftp.retrbinary("RETR " + filename, file.write)
    

def initftp(ftpHost):
    ftp = FTP(ftpHost)
    ftp.login()
    return ftp



if __name__=="__main__":
    main()