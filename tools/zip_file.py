# -*- coding: UTF-8 -*-
import os
import zipfile


def zip_compress(to_zip,save_zip_name):
    # save_zip_name是带目录的，也可以不带就是当前目录
    #1.先判断输出save_zip_name的上级是否存在(判断绝对目录)，否则创建目录
    #save_zip_name的上级目录
    save_zip_dir=os.path.split(os.path.abspath(save_zip_name))[0]

    if not os.path.exists(save_zip_dir):
        os.makedirs(save_zip_dir)
        print('创建新目录%s' % save_zip_dir)
    f = zipfile.ZipFile(os.path.abspath(save_zip_name), 'w', zipfile.ZIP_DEFLATED)
    # 2.判断要被压缩的to_zip是否目录还是文件，是目录就遍历操作，是文件直接压缩
    # 如果不是目录,那就是文件
    if not os.path.isdir(os.path.abspath(to_zip)):
        # 判断文件是否存在
        if os.path.exists(os.path.abspath(to_zip)):
            f.write(to_zip)
            f.close()
            print('%s压缩为%s' % (to_zip, save_zip_name))
        else:
            print ('%s文件不存在' % os.path.abspath(to_zip))
    else:
        # 判断目录是否存在，遍历目录
        if os.path.exists(os.path.abspath(to_zip)):
            zipList = []
            # 遍历目录，加入列表
            for dir,subdirs,files in os.walk(to_zip):
                for fileItem in files:
                    zipList.append(os.path.join(dir,fileItem))
                    # print('a',zipList[-1])
                for dirItem in subdirs:
                    zipList.append(os.path.join(dir,dirItem))
                    # print('b',zipList[-1])
            #读取列表压缩目录和文件
            for i in zipList:
                # replace是减少压缩文件的一层目录，即压缩文件不包括to_zip这个目录
                f.write(i,i.replace(to_zip,''))
                # print('%s压缩到%s'%(i,save_zip_name))
            f.close()
            print('%s压缩为%s' % (to_zip, save_zip_name))
        else:
            print('%s文件夹不存在' % os.path.abspath(to_zip))


if __name__ == '__main__':
    zip_compress("", "")
