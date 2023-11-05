# @python  : 3.11.0
# @Time    : 2023/11/03
# @Author  : Shadow403
# @Version : 0.1.0
# @Email   : admin@shadow403.cn
# @Software: Visual Studio Code

"""
API File
"""

from . import draw
import requests, json
from jsonpath import jsonpath
requests.packages.urllib3.disable_warnings()

class biliAPI:
    """
    `API_URL`: https://api-dev.shadow403.cn
    """

    def __init__(self):
        self.url = "https://api-dev.shadow403.cn/api/bilibili"

    def userMedalInfo(self, UID:str):
        """
        Get Medal `ID` `Name`
        """
        try:
            getMedalJson = json.loads(requests.get(f"{self.url}/user/medal/all/{UID}").text)
        except Exception as ErrorGetMedalInfo:
            return [-2, f"{str(ErrorGetMedalInfo)}"]

        if (getMedalJson["code"] == 200):
            userName = getMedalJson["data"]["name"]
            userLevel = getMedalJson["data"]["level"]
            userFaceUrl = getMedalJson["data"]["icon"]
            
            if (getMedalJson["data"]["count"] != 0):
                userAllMedalName = jsonpath(getMedalJson, "$.data.list[*].medal_info.medal_name")
                userAllMedalLevel = jsonpath(getMedalJson, "$.data.list[*].medal_info.level")
                MedalAllInfo = [list(item) for item in zip(userAllMedalName, userAllMedalLevel)]
                results = draw.baseDraw([0, [userName, UID, userLevel, userFaceUrl, MedalAllInfo]])
                return results
            else:
                results = draw.baseDraw([-1, [userName, UID, userLevel, userFaceUrl]])
                return results

        else:
            results = draw.baseDraw([-2, getMedalJson['message']])
            return results