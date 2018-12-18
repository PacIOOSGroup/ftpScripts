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
      sys.exit()


    filename1 = "adp5_"+str(now.year)+str(now.month)+str(now.day-1)+"_00_08.nc"
    filename2 = "adp5_"+str(now.year)+str(now.month)+str(now.day-1)+"_08_16.nc"
    filename3 = "adp5_"+str(now.year)+str(now.month)+str(now.day-1)+"_16_24.nc"

    ftp.cwd("pub/aco/adp/" + str(now.year) + "/" +str(now.month))

    with open(filename1, "wb") as file: ftp.retrbinary("RETR " + filename1, file.write)
    with open(filename2, "wb") as file: ftp.retrbinary("RETR " + filename2, file.write)
    with open(filename3, "wb") as file: ftp.retrbinary("RETR " + filename3, file.write)


def initftp(ftpHost):
    ftp = FTP(ftpHost)
    ftp.login()
    return ftp



if __name__=="__main__":
    main()