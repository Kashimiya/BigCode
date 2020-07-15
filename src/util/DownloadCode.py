#下载并解压后的代码文件存放在"D:\\bigCodeDownloads\\unziped\\"中
import json
import urllib.request
import urllib.parse
import os
import zipfile

f = open('D:\\test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
dir="D:\\bigCodeDownloads\\raw\\"
dir_target="D:\\bigCodeDownloads\\unziped\\"
selected_uid=[60686,60782,60586,60690,60771,40552,60595,60749,60678,60721,60810,59140,60637,60660,60746,60825]
selected_num=[19,32,54,72,92,104,114,133,179,184,196,237,242,245,255,260]
# print(data)
for i in range(len(selected_num)):
    uid=str(selected_uid[i])
    user="no"+str(selected_num[i])+"_uid"+str(selected_uid[i])
    cases = data[uid]['cases']
    print(cases)
    # 下载选定用户的最终提交代码到D:\\bigCodeDownloads
    for case in cases:
        #下载
        print(case["case_id"], case["case_type"], case['case_zip'])
        # filename为保存到本地的文件名
        filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
        filename=filename.replace("*","x")

        isExists_user= os.path.exists(dir + user)#检查用户id文件夹是否存在
        if not isExists_user:
            os.makedirs(dir + user)
        isExists_type = os.path.exists(dir + user+"\\"+case["case_type"])#检查题目类型文件夹是否存在
        if not isExists_type:
            os.makedirs(dir+user+"\\"+case["case_type"])
        filename = dir + user + "\\" + case["case_type"]+"\\"+filename
        print(filename)
        urllib.request.urlretrieve(urllib.parse.quote(case["case_zip"], ":?/.-"), filename)

        #解压缩
        isExists_user = os.path.exists(dir_target + user)  # 检查用户id文件夹是否存在
        if not isExists_user:
            os.makedirs(dir_target + user)
        isExists_type = os.path.exists(dir_target + user + "\\" + case["case_type"])  # 检查题目类型文件夹是否存在
        if not isExists_type:
            os.makedirs(dir_target + user + "\\" + case["case_type"])
        filename_target = urllib.parse.unquote(os.path.basename(case["case_zip"]))
        filename_target = filename_target.replace("*", "x")
        filename_target=dir_target + user + "\\" + case["case_type"]+"\\"+filename_target
        f=zipfile.ZipFile(filename,'r')
        print(f.namelist())
        for file in f.namelist():
            if file=='.mooctest/answer.py' or file=='.mooctest/testCases.json':
                f.extract(file,filename_target)

