import requests
import xml.etree.ElementTree as ET

class Metar:
    base_url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=3&mostRecent=true&stationString="
    def __init__(self, station_code):
        self.station_code = station_code

    def get_weather(self):
        url = self.base_url + self.station_code
        r = self.__request_weather(url)
        metar_str = self.__parse_metar_xml(r)
        return metar_str

    def __request_weather(self, url):
        r = requests.get(url)
        return r.content

    def __parse_metar_xml(self, content):
        root = ET.fromstring(content)
        metar_element = root.find('data/METAR/raw_text')
        if metar_element is None:
            return None
        return metar_element.text