import requests
import re
import os
import urllib

URL = "https://www.arpa.veneto.it/bollettini/meteo/radar/index_geo.php"
REGEX = r"imgs/mosaico/(mosaico_[a-zA-Z0-9_.]+)"

response = requests.get(URL)

print("Request has code {}".format(response.status_code))

# two groups enclosed in separate ( and ) bracket
filenames = re.findall(REGEX, response.text)

for filename in filenames:

    # image_url = imgs/mosaico/mosaico_202107131240_mpgrid_CZ_c_mbasemax_6510858a0270815072a151850238f3_G.png

    # https://www.arpa.veneto.it/bollettini/meteo/radar/imgs/mosaico/mosaico_202107131320_mpgrid_CZ_c_mbasemax_291966d8209f7cf3442d8aa90ec0f2_G.png
    image_url = "https://www.arpa.veneto.it/bollettini/meteo/radar/imgs/mosaico/" + filename
    print(image_url)


     # Download the file if it does not exist
    if not os.path.isfile(filename):

        print('Downloading: ' + filename)
        try:
            urllib.request.urlretrieve(image_url, filename)
        except Exception as inst:
            print(inst)
            print('  Encountered unknown error. Continuing.')

    else:
        print('Already downloaded: ' + filename)
