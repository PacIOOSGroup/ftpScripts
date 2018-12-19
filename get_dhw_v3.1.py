#!/usr/bin/python3

from ftplib import FTP
import datetime
import os
import sys

def main():
    now = datetime.datetime.now()
    filedir = "/export/data/dhw_v3.1/"
    ftpHost="ftp.star.nesdis.noaa.gov"
    ftp = initftp(ftpHost)

    currentDate = str(now.year)+str(now.month)+str(now.day-1)

    try:
        os.chdir(filedir)
    except:
        print("some error accessing directory (does it exist?)")
        print("you tried:%s" % filedir)
    #    try:
     #       os.makedir(filedir)
      #  except:
       #     print("failed to create directory, perhaps out of space or lack permissions.") 
        #    sys.exit()

    folders = ["sst", "dhw", "hs", "ssta", "baa"]
    filenames = ["coraltemp_v1.0_" + currentDate + ".nc", "ct5km_dhw_v3.1_" + currentDate + ".nc", 
        "ct5km_hs_v3.1_" + currentDate + ".nc", "ct5km_ssta_v3.1_" + currentDate + ".nc", "ct5km_baa_v3.1_" + currentDate + ".nc"]

    ftpTopLevelDir = "/pub/socd/mecb/crw/data/5km/v3.1/nc/v1.0/daily"
    
    for i in range(0, len(folders)):

        ftp.cwd(ftpTopLevelDir)        
        ftp.cwd(folders[i])
        ftp.cwd(str(now.year))
        with open(filenames[i], "wb") as file: ftp.retrbinary("RETR " + filenames[i], file.write)

def initftp(ftpHost):
    ftp = FTP(ftpHost)
    ftp.login()
    return ftp

if __name__=="__main__":
    main()
