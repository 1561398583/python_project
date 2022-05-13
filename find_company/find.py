

def decode():
    f = open('E:\\python_work\\find_company\\companyInfos', "r")

    infos = []

    line = f.readline()
    while line:
        info = {}
        ss = line.split(', ')
        for item in ss:
            s2 = item.split(': ')
            info[s2[0]] = s2[1]
        infos.append(info)
        line = f.readline()

    f.close()
    return infos


infos = decode()
for info in infos:
    if info['status'] == '吊销':
        print(info)
        print('\n')





