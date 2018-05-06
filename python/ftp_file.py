# coding=utf-8
'''该方法用于递归计算文件夹内的各个文件和文件夹的大小'''
import os


def getdirsize(file_path, size=0):
    '''递归方式获取文件的体积'''
    if os.path.isfile(file_path):
        size = os.path.getsize(file_path)
    else:
        for root, dirs, files in os.walk(file_path):
            for temf in files:
                size += os.path.getsize(os.path.join(root, temf))
                # print "file:" + temf
    return size


# print 'size of directory:' + str(getdirsize(r"E:/capture"))


def dirdetail(dir_root=None, tar_size=1024, tar_unit=2):
    '''dir_root是操作的文件夹根目录，建议格式如dir_root=r'C:'。
    tar_size是储存容量的进制，默认是windows采用的1024进制，unix和linux采用的则是1000进制
    tar_unit是进行筛选的单位，0代表byte,1代表KB,2代表MB，3代表GB，而其他的单位在打印时不显示，默认1024byte^2=1MB。'''
    with open('./logs/result.txt', 'w') as refile:
        refile.write('search result:\n')

    dir_list = []
    dir_total = os.listdir(dir_root)
    if tar_unit == 0:
        dispaly_unit = 'byte'
    elif tar_unit == 1:
        dispaly_unit = 'KB'
    elif tar_unit == 2:
        dispaly_unit = 'MB'
    elif tar_unit == 3:
        dispaly_unit = 'GB'
    else:
        dispaly_unit = ''

    [dir_list.append(os.path.join(dir_root, d)) for d in dir_total]

    for tem in dir_list:
        tem_size = getdirsize(tem)
        if tem_size > tar_size**tar_unit:
            with open('./logs/result.txt', 'a') as refile:
                print tem
                refile.write(tem + '\t\tsize:' +
                             str(round(float(tem_size) / (tar_size**tar_unit), 2)) + ' ' + dispaly_unit + '\n')


if __name__ == '__main__':
    dirdetail(dir_root=r'E:\BaiduNetdiskDownload', tar_size=1024, tar_unit=0)
