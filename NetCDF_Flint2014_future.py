'''   URLRetrieve for the Flint 2014
          California Basin Model
              ~Future~ Version:
		  http://cida.usgs.gov/thredds/dodsC/CA-BCM-2014/future.html
		  
        This simple script iterates through the
        available data.  It places the files in the 
		same directory from which it is invoked.

        8/8/2014
        
       Daryl Van Dyke
       Klamath Strategic Habitat Conservation Team
       GIS Analyst
       daryl_van_dyke@fws.gov
       
'''
import urllib,os

#  CHANGE ME for output somewhere other than where the script is called

strOutputDir = ""  # make sure the path ends in /


urlStart = "http://cida.usgs.gov/thredds/fileServer/CA-BCM-2014/HST/Monthly/"
urlPart1 = "http://cida.usgs.gov/thredds/fileServer/CA-BCM-2014/"
urlPart2 = "Monthly"

listModels = ['GFDL', 'PCM', 'MIROC3_2', 'CSIRO', 'GISS_AOM','MIROC5',
              'MIROC' , 'GISS', 'MRI', 'MPI', 'CCSM4', 'IPSL', 'CNRM', 'FGOALS']

listFolders = ["PCM_A2/","MRI_rcp26/","MPI_rcp45/","MIROC_rcp85/","MIROC_rcp60/",
               "MIROC_rcp45/","MIROC5_rcp26/","GISS_rcp26/","GISS_AOM_A1B/",
               "GFDL_B1/","GFDL_A2/","FGOALS_rcp85/","CSIRO_A1B/","CNRM_rcp85/",
               "CCSM4_rcp85/"]  #  ,"HST/"  - Already in Historic Script

#  example for pattern matching
#_________'CA_BCM_HST_Monthly_tmx_2010.nc'
#          CA_BCM_CSIRO_A1B_Monthly_tmx_2099.nc
#http://cida.usgs.gov/thredds/fileServer/CA-BCM-2014/PCM_A2/Monthly/CA_BCM_PCM_A2_Monthly_tmx_2007.nc

filePart1='CA_BCM_'
#                  _model___
filePart2=                "_Monthly_"
#                                    Ps_
listYears = range(2007,2100)#    YEAR
filePart3=                                 ".nc"

listPs = ['tmx', 'tmn', 'str', 'snw', 'run', 'rch' , 'ppt' ,
          'pet' , 'exc' , 'cwd', 'aet']
###################################################################################

fileNC = urllib.URLopener()

for model in listFolders:
    for param in listPs:
        for year in listYears:
            strFile = filePart1 + model[:-1] + filePart2 + param + '_' + str(year) + filePart3
            strURLhead = urlPart1+model+urlPart2
            print "Starting", strFile, "from",strURLhead+'/'+strFile
            fileNC.retrieve(strURLhead+'/'+strFile, strFile)
        
