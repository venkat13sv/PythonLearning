import os
def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            fsize=os.path.getsize(fp)
            if fsize < 1048576:
                print("File Info {0} size={1} KB".format(fp,(fsize/1024)))
                print(fsize/1024)
            else:
                print("File Info {0} size={1} MB".format(fp,(fsize/(1024*1024))))
            total_size += os.path.getsize(fp)
    return total_size

print("Total Size:{0}".format(get_size("E:\Personal Documents")))
