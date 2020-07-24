# 下载并解压后的代码文件存放在"D:\\bigCodeDownloads\\unziped\\"中
import json
import urllib.request
import urllib.parse
import os
import zipfile

# 懒得写接口了！有人帮忙写下吗？ 要用的时候改一下路径吧
class DownloadCode:
    selected_uid=[]

    def __init__(self,selected_uid):
        self.selected_uid=[]
        self.selected_uid.append(int(selected_uid))
    def download(self):
        dir = "D:\\bigCodeDownloads\\raw\\"
        dir_target = "D:\\bigCodeDownloads\\unziped\\"
        f = open('D:\\test_data.json', encoding='utf-8')
        res = f.read()
        data = json.loads(res)
        # print(data)
        for i in range(len(self.selected_uid)):
            uid = str(self.selected_uid[i])
            user ="uid_" + str(self.selected_uid[i])
            cases = data[uid]['cases']
            print(cases)
            # 下载选定用户的最终提交代码到D:\\bigCodeDownloads
            i = 1
            for case in cases:
                # 下载
                if(int(case['final_score'])==0):
                    continue
                print(case["case_id"], case["case_type"], case['case_zip'])
                # filename为保存到本地的文件名
                filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
                filename = filename.replace("*", "x")
                filename = uid + "_" + case["case_id"] + "_" + filename

                isExists_user = os.path.exists(dir + user)  # 检查用户id文件夹是否存在
                if not isExists_user:
                    os.makedirs(dir + user)
                isExists_type = os.path.exists(dir + user + "\\" + case["case_type"])  # 检查题目类型文件夹是否存在
                if not isExists_type:
                    os.makedirs(dir + user + "\\" + case["case_type"])
                filename = dir + user + "\\" + case["case_type"] + "\\" + filename
                print(filename)
                print(urllib.parse.quote(case['upload_records'][-1]["code_url"], ":?/.-"))
                urllib.request.urlretrieve(case['upload_records'][-1]["code_url"], filename)

                # 解压缩
                isExists_user = os.path.exists(dir_target + user)  # 检查用户id文件夹是否存在
                if not isExists_user:
                    os.makedirs(dir_target + user)
                isExists_type = os.path.exists(dir_target + user + "\\" + case["case_type"])  # 检查题目类型文件夹是否存在
                if not isExists_type:
                    os.makedirs(dir_target + user + "\\" + case["case_type"])
                filename_target = urllib.parse.unquote(os.path.basename(case["case_zip"]))
                filename_target = filename_target.replace("*", "x")
                filename_target = uid + "_" + case["case_id"] + "_" + filename_target
                filename_target = dir_target + user + "\\" + case["case_type"] + "\\" + filename_target


                f_temp = zipfile.ZipFile(filename, 'r')
                # print(f.namelist())

                zip_temp = "D:\\BigCodeDownloads\\zip_temp"
                print(f_temp.namelist())
                name_temp = ""
                for file in f_temp.namelist():
                    f_temp.extract(file, zip_temp + "\\" + str(i))
                    name_temp = file
                f = zipfile.ZipFile(zip_temp + "\\" + str(i) + "\\" + name_temp, 'r')
                for file in f.namelist():
                    if file == 'main.py' or file == '.mooctest/testCases.json':
                        f.extract(file, filename_target)
                i += 1
