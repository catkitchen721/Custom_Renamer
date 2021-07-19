import os

DIR_TO_CONVERT_TARGET = 'TO_CONVERT_TARGET'

root_dir = os.path.split(os.path.realpath(__file__))[0]
target_dir = os.path.join(root_dir, DIR_TO_CONVERT_TARGET)
target_list = os.listdir(target_dir)

if len(target_list) <= 0:
    print('No files or directories')
    exit()

if len(target_list) == 1:
    target_name = target_list[0]
    target = os.path.join(target_dir, target_list[0])
else:
    print('Which target do you want to rename?')
    print(target_list)
    target = input()
    while (not target in target_list) and target != '/exit' :
        print('No target:', f'"{target}"')
        print('Try again or input "/exit" to exit.')
        target = input()
    if target == '/exit':
        exit()
    target_name = target
    target = os.path.join(target_dir, target)

if os.path.isdir(target):
    print(target_name, 'is a directory.')
    isDirectory = True
else:
    print(target_name, 'is a file.')
    isDirectory = False

if not isDirectory:
    exit()
else:
    target_files = os.listdir(target)
    print('Files Preview:')
    if len(target_files) <= 3:
        print(target_files)
    else:
        print("['"+target_files[0]+"', "+"'"+target_files[1]+"', "+"'"+target_files[0]+"', ...]")
    print("NOT to rename ext:(if rename all, just ENTER)")
    no_ext = input()
    print("mode: [cut, ]")
    mode = input()
    if mode == 'cut':
        c1 = input('cut from:(sub string)')
        d1 = input('search from left/right:(l/r)')
        r1 = input('remain this string or not:(y/n)')
        c2 = input('to:(sub string)')
        d2 = input('search from left/right:(l/r)')
        r2 = input('remain this string or not:(y/n)')
        for fname in target_files:
            if os.path.splitext(fname)[1] != ('.'+no_ext if no_ext[0] != '.' else no_ext):
                if d1 == 'l' or d1 == 'L':
                    i1 = fname.find(c1)
                else:
                    i1 = fname.rfind(c1)
                if r1 == 'y' or r1 == 'Y':
                    i1 += len(c1)
                if d2 == 'l' or d2 == 'L':
                    i2 = fname.find(c2)
                else:
                    i2 = fname.rfind(c2)
                if r2 == 'n' or r2 == 'N':
                    i2 += len(c2)
                newname = fname[:i1] + fname[i2:]
                os.rename(os.path.join(target, fname), os.path.join(target, newname))
        print('Rename', target, 'successful.')
    else:
        pass