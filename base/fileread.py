
def get_lines():
    with open('file.txt', 'rb') as f:
        for i in f:
            yield i

def get_lines2(fp):
    from mmap import mmap
    with open(fp,'r+') as f:
        m = mmap(f.fileno(), 0)
        for i, char in enumerate(m):
            if char == b'\n':
                yield m[tmp:i+1].decode()
                tmp = i+1


def find_file(s_path):
    import os
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            find_file(s_child_path)
        else:
            print(s_child_path)

def findSuffix(dir, suffix):
    import os
    res = []
    for root,dir,files in os.walk(dir):
        for filename in files:
            name, suf = os.path.splitext(filename)
            if suf == suffix:
                res.append(os.path.join(root, filename))
    return res

def findSuffix2(path, suffix):
    import os
    file_list = os.listdir(path)
    for obj in file_list:
        if os.path.isfile(obj):
            try:
                if obj[-4:] == suffix:
                    print(obj)
            except:
                pass
        elif os.path.isdir(obj):
            findSuffix2(obj, suffix)


def findSuffix3(path,suffix):
    from glob import iglob
    for i in iglob(f"{path}/**/*{suffix}", recursive=True):
        print(i)

if __name__ == '__main__':
    find_file('/home/feng/code_exercise/')