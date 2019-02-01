import os


def walk(directory):
    names = []
    for name in os.listdir(directory):
        path = os.path.join(directory, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))

    return names


def pipe(command):
    
    fp = os.popen(command)
    result = fp.read()
    stat = fp.close()

    assert stat is None

    return result, stat



def md5_checksum(file):
    

    command = 'md5 ' + file


    return pipe(command)


def check_diff(file1, file2):
    
    command = 'diff %s %s' % (file1, file2)

    return pipe(command)

def compute_checksums(directory, suffix):
    d = {}
    

    names = walk(directory)

    for name in names:
        if name.endswith(suffix):
            result, _ = md5_checksum(name)
            resultList = result.split()

            checksum = resultList[-1]

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d
('MD5 (./ch9/9_8.py) = b82d2b230b128f11a2db348919106458\n', None)



def check_pairs(names):

    for name in names:
        for name1 in names:
            if name < name1:
                result, stat = check_diff(name, name1)

                if result:
                    return False

    return True


def print_doubles(d):
    
    for key, values in d.items():
        if len(values) > 1:
            print("The following files have identical checksums:")
            for value in values:
                print(value)
            if check_pairs(values):
                print("and they are identical.")



if __name__ == '__main__':
    
    d = compute_checksums(directory='.', suffix='.py')
    print_doubles(d)
