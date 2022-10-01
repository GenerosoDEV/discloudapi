import requests

url = "https://api.discloud.app/v2"

def formatReturn(result): 
    result_json = result.json()
    result_json["rateLimit"] = result.headers["ratelimit-limit"]
    result_json["rateLimitRemaining"] = result.headers["ratelimit-remaining"]
    result_json["rateLimitReset"] = result.headers["ratelimit-reset"]
    return result_json

class Client:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.headers={"api-token":self.api_token}

    # USER AREA
    def user(self):
        result = requests.get(url+"/user", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def locale(self, locale: str):
        result = requests.put(url+f"/locale/{locale}", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def upload(self):
        result = requests.post(url+f"/upload", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    # APP AREA

    def app(self, app_id: str):
        result = requests.get(url+f"/app/{app_id}", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appStatus(self, app_id: str):
        result = requests.get(url+f"/app/{app_id}/status", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appLogs(self, app_id: str):
        result = requests.get(url+f"/app/{app_id}/logs", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appStart(self, app_id: str):
        result = requests.put(url+f"/app/{app_id}/start", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appRestart(self, app_id: str):
        result = requests.put(url+f"/app/{app_id}/restart", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appStop(self, app_id: str):
        result = requests.put(url+f"/app/{app_id}/stop", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appCommit(self, app_id: str):
        result = requests.put(url+f"/app/{app_id}/commit", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appDelete(self, app_id: str):
        result = requests.delete(url+f"/app/{app_id}/delete", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appBackup(self, app_id: str):
        result = requests.get(url+f"/app/{app_id}/backup", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appRamUpdate(self, app_id: str, ramMB: int):
        result = requests.put(url+f"/app/{app_id}/ram", headers=self.headers, json={"ramMB": ramMB})
        result_json = formatReturn(result)
        return result_json

    # TEAM AREA
    
    def team(self):
        result = requests.get(url+f"/team", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appTeamStatus(self, app_id: str):
        result = requests.get(url+f"/team/{app_id}/status", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appTeamLogs(self, app_id: str):
        result = requests.get(url+f"/team/{app_id}/logs", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appTeamStart(self, app_id: str):
        result = requests.put(url+f"/team/{app_id}/start", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appTeamRestart(self, app_id: str):
        result = requests.put(url+f"/team/{app_id}/restart", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appTeamStop(self, app_id: str):
        result = requests.put(url+f"/team/{app_id}/stop", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appTeamCommit(self, app_id: str):
        result = requests.put(url+f"/team/{app_id}/commit", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appTeamBackup(self, app_id: str):
        result = requests.get(url+f"/team/{app_id}/backup", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def appTeamRamUpdate(self, app_id: str, ramMB: int):
        result = requests.put(url+f"/team/{app_id}/ram", headers=self.headers, json={"ramMB": ramMB})
        result_json = formatReturn(result)
        return result_json

    # MOD AREA

    def mod(self, app_id: str):
        result = requests.get(url+f"/app/{app_id}/team", headers=self.headers)
        result_json = formatReturn(result)
        return result_json

    def addMod(self, app_id: str, mod_id: int, permissions: list):
        result = requests.post(url+f"/app/{app_id}/team", headers=self.headers, json={"modID": mod_id, "perms":permissions})
        result_json = formatReturn(result)
        return result_json

    def editMod(self, app_id: str, mod_id: int, permissions: list):
        result = requests.put(url+f"/app/{app_id}/team", headers=self.headers, json={"modID": mod_id, "perms":permissions})
        result_json = formatReturn(result)
        return result_json
        
    def deleteMod(self, app_id: str, mod_id: int):
        result = requests.delete(url+f"/app/{app_id}/team/{mod_id}", headers=self.headers)
        result_json = formatReturn(result)
        return result_json