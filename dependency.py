import os

def all_path(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)
            result.append(apath)
    return result

if __name__ == '__main__':
    print('hello')
    GDMEditTools = '/Users/holiday/Library/Workspace/Gaoding-iOS/modules/GDMEditTools/GDMEditTools/Classes'
    GDEditor = '/Users/holiday/Library/Workspace/Gaoding-iOS/modules/GDEditor/GDEditor'

    print(GDMEditTools)
    print(GDEditor)

    # 待检查文件
    GDMEditToolsSubFiles = []
    for path in all_path(GDMEditTools):
        (path, filename) = os.path.split(path)
        GDMEditToolsSubFiles.append(filename.split('.')[0])

    for r in GDMEditToolsSubFiles:
        print(r)

    # 便利所有文件内容，检查是否包含带检查文件
    result = []
    for path in all_path(GDEditor):
        if '.m' in path or '.h' in path:
            # print(path)
            f = open(path)
            line = f.readline()
            while line:
                line = f.readline()
                if '//' not in line:
                    # print(line)
                    for ddd in GDMEditToolsSubFiles:
                        if len(ddd) > 0:
                            if ddd+'.h' in line:
                                (path, filename) = os.path.split(path)
                                result.append(filename.split('.')[0])
                                print('检查', ddd, 'ddd')
                                print('对比', line, '文件', filename)
                                break
            f.close()
    
    result = set(result)
    for r in result:
        print(r)

    