import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

usernameAnaplan = str(os.getenv("usernameAnaplan"))
passwordAnaplan = str(os.getenv("passwordAnaplan"))

workspaceAnaplan = str(os.getenv("workspaceID"))
modelsAnaplan = str(os.getenv("modelsID"))
listIDAnaplan = str(os.getenv("listID"))


def tokenAnaplan():
    basicToken = 'Basic '+str(base64.b64encode((f'{usernameAnaplan}:{passwordAnaplan}')
                                               .encode('latin-1')).decode('latin-1'))
    
    getHeaders = {'Authorization': basicToken}

    getTokenAnaplan =  requests.post('https://auth.anaplan.com/token/authenticate', headers=getHeaders)

    getTokenAnaplanResponse = getTokenAnaplan.json()
    tokenAnaplan = getTokenAnaplanResponse['tokenInfo']['tokenValue']
    return tokenAnaplan

tokenAnaplan()

#try getListItems using token Anaplan
tokenAnaplan =  tokenAnaplan()
getListItems = requests.get(f'https://api.anaplan.com/2/0/workspaces/{workspaceAnaplan}/models/{modelsAnaplan}/lists/{listIDAnaplan}/items?includeAll=true', 
                            headers={'Content-Type':'application/json', 'Accept': 'application/json', 'Authorization': f'AnaplanAuthToken {tokenAnaplan}'})
print(getListItems.content)






