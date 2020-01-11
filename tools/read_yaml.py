import  yaml
import os

from config import BaseURL


def readyaml(filename):
    with open(BaseURL+os.sep+'data'+os.sep+filename,"r",encoding="utf8")as f:
        arr =[]
        for data in yaml.load(f).values():
            arr.append(tuple(data.values()))
        return  arr