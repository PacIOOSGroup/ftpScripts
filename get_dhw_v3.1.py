#!/usr/bin/python3

from ftplib import FTP
import datetime
import os
import sys
from subprocess import run

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
    outfile = "merged_ct5km_v3.1_" + currentDate + ".nc"
    ftpTopLevelDir = "/pub/socd/mecb/crw/data/5km/v3.1/nc/v1.0/daily"
    
    for i in range(0, len(folders)):

        ftp.cwd(ftpTopLevelDir)        
        ftp.cwd(folders[i])
        ftp.cwd(str(now.year))
        with open(filenames[i], "wb") as file: ftp.retrbinary("RETR " + filenames[i], file.write)
    
    run(["/usr/bin/ncpdq", "-a", "-lat", filenames[0], "temp.nc"])
    run(["mv", "temp.nc", filenames[0]])

    run(["cp", filenames[1], outfile)

    run(["/usr/bin/ncks", "-A", filenames[2], outfile])
    run(["/usr/bin/ncks", "-A", filenames[0], outfile])
    run(["/usr/bin/ncks", "-A", filenames[3], outfile])
    run(["/usr/bin/ncks", "-A", filenames[4], outfile])

    run(["/usr/bin/ncrename", "-v", "analysed_sst,CRW_SST", outfile])
    run(["/usr/bin/ncrename", "-v", "bleaching_alert_area,CRW_BAA", outfile])
    run(["/usr/bin/ncrename", "-v", "hotspot,CRW_HOTSPOT", outfile])
    run(["/usr/bin/ncrename", "-v", "degree_heating_week,CRW_DHW", outfile])
    run(["/usr/bin/ncrename", "-v", "sea_surface_temperature_anomaly,CRW_SSTANOMALY", outfile])
    run(["/usr/bin/ncrename", "-v", "sea_ice_fraction,CRW_SEAICE", outfile])
    run(["/usr/bin/ncrename", "-v", "mask,surface_flag", outfile])
    
    run(["/usr/bin/ncatted", "-O", "-a", "epsg_code,crs,o,c,EPSG:4326", outfile])
    run(["/usr/bin/ncatted", "-O", "-a", "geospatial_bounds_crs,global,o,c,EPSG:4326", outfile])

    run(["mv", outfile, str(now.year)])



def initftp(ftpHost):
    ftp = FTP(ftpHost)
    ftp.login()
    return ftp

if __name__=="__main__":
    main()
