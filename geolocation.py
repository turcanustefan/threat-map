import geoip2.database
import requests
import xml.etree.cElementTree as ET
import itertools
import keyring

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# def get_data_from_siem(siem_ip):
#     time = ''
#     src_ip = ''
#     src_port = ''
#     return time, src_ip, src_port


# db = geoip2.database.Reader('GeoLite2-Country.mmdb')


#while True:
#src_ip, src_port = get_data_from_siem()
# country = db.country('113.109.111.211') # src_ip
# print(country.country) # iso_code

# Credentials
service_id = 'THREAT_MAP'
username = 'sturcanu'
password = keyring.get_password(service_id, username)


def getRealTimeConnections():
    # Get authentication token
    proxies = {"http": "", "https": "", "ftp": ""}
    api = requests.get("https://10.1.2.70:8443/www/core-service/rest/LoginService/login?login={}&password={}".format(username, password), verify=False, proxies=proxies)

    authxml = api.text
    root = ET.fromstring(authxml)
    child = root[0]
    authkey = child.text

    api = requests.get("https://10.1.2.70:8443/www/manager-service/rest/QueryViewerService/getMatrixData?authToken=%s&id=RESOURCE_ID" % authkey, proxies=proxies, verify=False)

    raw_data = api.text
    xml_data = ET.XML(raw_data)
    data = xml_data.iter()

    for i in xrange(1,18):
        dummy = data.next().text

    while True:
        try:
            dummy = data.next().text
            ts = data.next().text
            name = data.next().text
            msg = data.next().text
            dip = data.next().text
            sip = data.next().text
            prod = data.next().text
            vendor = data.next().text
            proto = data.next().text
            itype = data.next().text
            print("%s,%s,%s,%s,%s,%s,%s,%s,%s" % (ts,name,msg,dip,sip,prod,vendor,proto,itype))
        except:
            break

#getRealTimeConnections()