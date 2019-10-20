import os
from configparser import ConfigParser
import json


class ConfigSetting():
    '''load config in ini type file'''
    def __init__(self, file_path='', conf_type=''):
        self.__file_path = file_path
        self.__type = conf_type
        self.config_list = []
        self.__load()

    def __load(self):
        self.config = ConfigParser()
        self.config.read(self.__file_path, encoding='UTF-8')
        self.config_list = self.config.sections()
        # print('sections:', self.config.sections())
        return self.config_list

    def getSections(self):
        return self.config_list

    def findOption(self,option):
        return self.config.items(option)

    def findKeyStr(self, section, key):
        return self.config.get(section,key)

    def findKeyInt(self, section, key):
        return self.config.getint(section,key)         
        

class WriteJson():
    '''use json file for data store'''
    def __init__(self, file_path='', conf_type=''):
        self.path = file_path
        self.conf = conf_type

    def writeLine(self, line):
        with open(self.path, 'w') as f:
            json.dump(line, f,indent=4)
            
    def loadLines(self):
        lines=[]
        with open(self.path, 'r') as f:
            for line in f.readlines():
                lines.append(json.load(line))            
        return lines
    
    def loadLine(self):
        with open(self.path, 'r') as f:
            lines=json.load(f)          
        return lines
          


def test_ini():
    local_path = os.getcwd() + r'\python\init_1.ini'
    print(local_path)
    configInit=ConfigSetting(local_path,'')
    init_sections=configInit.getSections()
    print(init_sections, type(init_sections))
    print(configInit.findOption(init_sections[0]))
    print(configInit.findKeyInt(init_sections[0], 'port'))

def test_json():
    json_path = os.getcwd() + r'\python\init.json'
    print(json_path)
    test_json = WriteJson(json_path)
    lines={}
    line = ["a", 123, 1]
    data_json = {}
    for i in range(100):
        lines[i] = line
    data_json["current data"]=lines
    test_json.writeLine(data_json)
    # print(lines,len(lines))
    print(json.dumps(test_json.loadLine(),indent=2))
    # print(test_json.loadLine())


test_json()    
