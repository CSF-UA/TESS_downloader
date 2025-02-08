'''
Code for downloading TESS ligthcurve data (cadence = 120 s) for each star from given sector
Code was created by New UA Astronomy Renaissance team (https://nuaar.com)
'''

# TessDataInterface for data downloading
from ramjet.data_interface.tess_data_interface import TessDataInterface
# for interacting with the operating system
import os



def get_list_of_stars(sector):
    '''
    Gets the list of all stars from .sh file in order to download data for each of them

    Parameters
    ----------
    sector : int
        the number of TESS sector

    Returns
    -------
    LOS : 
        list of stars (TIC numbers of the stars) in sector

    '''
    LOS = []
    f = open('tesscurl_sector_'+ str(sector) +'_lc.sh','r')
    S = f.readlines()[1:]
    f.close()
    for i in range(len(S)):
        a = S[i]
        a = S[i].split('-')
        LOS.append(int(a[6]))
    return LOS



def download_sector(sector):
    '''
    Downloads the data for each star from a certain sector

    Parameters
    ----------
    sector : int
        the number of TESS sector

    Returns
    -------
    None.

    '''
    PP = path+'/'+str(sector)
    if os.path.exists(PP) == False:
        os.mkdir(PP)
    count = len([name for name in os.listdir(PP) if os.path.isfile(os.path.join(PP, name))])
    LOS = get_list_of_stars(sector)
    for i in range(count, len(LOS)):
        try:
            TDI.download_two_minute_cadence_lightcurve(tic_id=LOS[i], sector=sector, save_directory=path+'/'+str(sector))
        except:
            print('ERROR')



path = os.getcwd()
TDI = TessDataInterface()
sector = int(input('Enter the sector number ->'))
download_sector(sector)
print('DONE!')