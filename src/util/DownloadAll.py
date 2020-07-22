# 下载并解压后的代码文件存放在"D:\\bigCodeDownloads\\unziped\\"中
import json
import urllib.request
import urllib.parse
import os
import zipfile

# 懒得写接口了！有人帮忙写下吗？ 要用的时候改一下路径吧
f = open('D:\\test_data.json', encoding='utf-8')
res = f.read()
data = json.loads(res)

quepath = os.path.abspath('../..') + '\\doc\\ChoosenQuestions.json'
file_que = open(quepath, encoding='utf-8')
que = file_que.read()
questions = json.loads(que)

dir = "D:\\bigCodeDownloads\\all\\raw\\"
dir_target = "D:\\bigCodeDownloads\\all\\unziped\\"
selected_uid = [60686, 60782, 60586, 60688, 60768, 61519, 60590, 60710, 60673, 60712, 60797, 59137, 60611, 60643, 60739,
                60825]
selected_num = [19, 32, 54, 72, 92, 104, 114, 133, 179, 184, 196, 237, 242, 245, 255, 260]
'''all = [3544, 48117, 49405, 51584, 60581, 60587, 60604, 60606, 60616, 60619, 60631, 60634, 60635, 60639, 60654, 60665,
       60671, 60676, 60686, 60707, 60708, 60715, 60737, 60752, 60760, 60762, 60763, 60769, 60772, 60773, 60775, 60782,
       60785, 60788, 60799, 60812, 60829, 60832, 60833, 60870, 60885, 60895, 60896, 60899, 61019, 61053, 61094, 61406,
       60615, 47329, 60598, 58834, 59018, 60586, 60589, 60602, 60603, 60613, 60620, 60621, 60627, 60632, 60636, 60642,
       60651, 60652, 60658, 60659, 60677, 60683, 60688, 60690, 60694, 60695, 60703, 60706, 60714, 60716, 60720, 60722,
       60724, 60725, 60730, 60733, 60738, 60742, 60753, 60756, 60759, 60764, 60768, 60771, 60787, 60790, 60827, 60828,
       60900, 60901, 61097, 61106, 61132, 61135, 61519, 40552, 61035, 61074, 60583, 39201, 48102, 58758, 59308, 60585,
       60590, 60595, 60599, 60617, 60624, 60630, 60638, 60641, 60647, 60653, 60657, 60661, 60666, 60668, 60669, 60675,
       60692, 60696, 60698, 60710, 60749, 60750, 60751, 60755, 60757, 60766, 60767, 60776, 60777, 60792, 60795, 60835,
       60837, 60846, 60876, 60889, 60898, 61041, 61659, 60645, 60679, 60700, 34511, 60711, 60866, 61212, 2843, 60578,
       49823, 60580, 60591, 60592, 60601, 60605, 60610, 60614, 60618, 60622, 60623, 60625, 60644, 60648, 60649, 60667,
       60670, 60673, 60678, 60691, 60697, 60699, 60712, 60721, 60723, 60731, 60747, 60765***, 60778, 60781, 60791, 60793,
       60794, 60796, 60797, 60810, 60836, 60839, 60891, 61046, 61048, 61715, 60628, 60713, 8160, 8246, 8317, 8318,
       16304, 39021, 39160, 39190, 39200, 40186, 47774, 47920, 47937, 47961, 48025, 48083, 48721, 49361, 49687, 50263,
       52592, 58547, 58575, 58585, 58586, 58610, 58616, 58634, 58778, 58822, 58865, 59137, 59140, 60593, 60594, 60608,
       60611, 60637, 60640, 60643, 60660, 60662, 60672, 60693, 60705, 60717, 60719, 60727, 60734, 60739, 60746, 60758,
       60761, 60770, 60774, 60825, 61020, 47996, 60689, 61143, 48090, 58744, 60584, 60728, 49315, 47879, 60822]'''
all=[60778, 60781, 60791, 60793,
       60794, 60796, 60797, 60810, 60836, 60839, 60891, 61046, 61048, 61715, 60628, 60713, 8160, 8246, 8317, 8318,
       16304, 39021, 39160, 39190, 39200, 40186, 47774, 47920, 47937, 47961, 48025, 48083, 48721, 49361, 49687, 50263,
       52592, 58547, 58575, 58585, 58586, 58610, 58616, 58634, 58778, 58822, 58865, 59137, 59140, 60593, 60594, 60608,
       60611, 60637, 60640, 60643, 60660, 60662, 60672, 60693, 60705, 60717, 60719, 60727, 60734, 60739, 60746, 60758,
       60761, 60770, 60774, 60825, 61020, 47996, 60689, 61143, 48090, 58744, 60584, 60728, 49315, 47879, 60822]
# selected_uid=[60739,60825]
# selected_num=[255,260]

# print(data)
for i in range(len(all)):
    uid = str(all[i])
    user = "uid_" + str(all[i])
    cases = data[uid]['cases']

    print(cases)
    # 下载选定用户的最终提交代码到D:\\bigCodeDownloads\\all
    for case in cases:

        category = ""
        print(case["case_id"], case["case_type"], case['case_zip'])
        # filename为保存到本地的文件名
        filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
        filename = filename.replace("*", "x")
        filename = uid + category + "_" + case["case_id"] + "_" + filename

        isExists_user = os.path.exists(dir + user)  # 检查用户id文件夹是否存在
        if not isExists_user:
            os.makedirs(dir + user)
        isExists_type = os.path.exists(dir + user + "\\" + case["case_type"])  # 检查题目类型文件夹是否存在
        if not isExists_type:
            os.makedirs(dir + user + "\\" + case["case_type"])
        filename = dir + user + "\\" + case["case_type"] + "\\" + filename
        print(filename)
        if(len(case['upload_records'])==0):
            break
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
        filename_target += category

        f_temp = zipfile.ZipFile(filename, 'r')
        # print(f.namelist())

        zip_temp = "D:\\BigCodeDownloads\\all\\zip_temp"
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