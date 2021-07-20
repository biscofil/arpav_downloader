import requests
import re
import os
import urllib

URL = "https://www.arpa.veneto.it/bollettini/meteo/radar/index_geo.php"
REGEX_URL = r"imgs/mosaico/(mosaico_[a-zA-Z0-9_.]+)"
REGEX_TIMESTAMP = r"mosaico_([0-9]+)_mpgrid_CZ_c_mbasemax_"

response = requests.get(URL)

print("Request has code {}".format(response.status_code))

filenames = re.findall(REGEX_URL, response.text)

for filename in filenames:

    # image_url = imgs/mosaico/mosaico_202107131240_mpgrid_CZ_c_mbasemax_6510858a0270815072a151850238f3_G.png

    # https://www.arpa.veneto.it/bollettini/meteo/radar/imgs/mosaico/mosaico_202107131320_mpgrid_CZ_c_mbasemax_291966d8209f7cf3442d8aa90ec0f2_G.png
    image_url = "https://www.arpa.veneto.it/bollettini/meteo/radar/imgs/mosaico/" + filename

    # only extract timestampt from the timestamp
    res = re.search(REGEX_TIMESTAMP, filename)
    filename = res.group(1) + '.png'

    # Download the file if it does not exist
    if not os.path.isfile(filename):

        print('Downloading ' + image_url + ' to ' + filename)
        try:
            urllib.request.urlretrieve(image_url, filename)
        except Exception as inst:
            print(inst)
            print(' > Encountered unknown error. Continuing.')

    else:
        print('Already downloaded: ' + filename)
