import os

path = 'E:\pdf'
print(os.listdir(path))
"""folders = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for folder in d:
        folders.append(os.path.join(r, folder))

for f in folders:
    print(f)"""
