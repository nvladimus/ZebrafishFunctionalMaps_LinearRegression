def bz2compressStack(name):
    import bz2
    with open(name, 'rb') as f:
        data = f.read()
    file = bz2.BZ2File(name + '.bz2', "wb")
    file.write(data)
    file.close()
    return

def bz2uncompressStack(name):
    import bz2
    file = bz2.BZ2File(name,'rb')
    data = file.read()
    file.close()
    stackFileName = name[:-4] #chopping the '.bz2' extension for raw file name
    with open(stackFileName, 'wb') as f:
        f.write(data)
    return
	