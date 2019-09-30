import requests
from bs4 import BeautifulSoup

url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
queryParams = '?'  + 'LAWD_CD=' + '11110' \
                + '&DEAL_YMD=' + '201811' \
                + '&serviceKey=' + 'zxerdxjycZVABMRMsqM6VCZ4d1u4IZPQjZ1QNN%2FGdGSGKTVJ9Z9jEEq9KLbVPTdJBDCqRMG1UGFaCeJM3PezhQ%3D%3D'

url = url + queryParams

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, "html.parser")

print(bs_obj)

