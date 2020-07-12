import json
import urllib.request
import urllib.parse
import os


f=open('D:\\test_data.json', encoding='utf-8')
res=f.read()
data=json.loads(res)
#print(data)

cases=data['3544']['cases']
print(cases)

#下载userid为3544的用户的最终提交代码到当前文件夹
for case in cases:
    print(case["case_id"], case["case_type"],case['case_zip'])
    #filename为保存到本地的文件名
    filename=urllib.parse.unquote(os.path.basename(case["case_zip"]))
    print(filename)
    urllib.request.urlretrieve(urllib.parse.quote(case["case_zip"],":?/.-"), filename)