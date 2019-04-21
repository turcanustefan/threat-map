import geoip2.database

# def get_data_from_siem(siem_ip):
#     time = ''
#     src_ip = ''
#     src_port = ''
#     return time, src_ip, src_port


db = geoip2.database.Reader('GeoLite2-Country.mmdb')


#while True:
#src_ip, src_port = get_data_from_siem()
country = db.country('113.109.111.211') # src_ip
print(country.country) # iso_code