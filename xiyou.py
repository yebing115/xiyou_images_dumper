#!/usr/bin/python
import sys
import struct
import uuid

file_name = 'images.dat'

class BlockInfo():
    def __init__(self, crc, offset, size, padding):
        self.crc = crc
        self.offset = offset
        self.size = size
        self.padding = padding

def getBlockInfos(file):
    blocks = []

    buf = file.read(0xc)
    count = struct.unpack_from('i', buf, 0x4)[0]
    offset = struct.unpack_from('i', buf, 0x8)[0]

    f.seek(offset)

    for i in range(count):
        tempBuf = file.read(0x10)
        tempCrc = tempBuf[0:0x4]
        tempOffset = struct.unpack_from('i', tempBuf, 0x4)[0]
        tempSize = struct.unpack_from('i', tempBuf, 0x8)[0]
        tempPadding = tempBuf[0xc:]
        blocks.append(BlockInfo(tempCrc, tempOffset, tempSize, tempPadding))

        offset += 0x10
        f.seek(offset)

    return blocks

def dumpFile(file, offset, size):
    file.seek(offset)
    content = file.read(size)
    f = open(str(uuid.uuid4()), 'wb')
    f.write(content)
    f.close()

def extractFile(file):
    blocks = getBlockInfos(file)

    for block in blocks:
        dumpFile(file, block.offset, block.size)

if __name__ == '__main__':
    file_name = sys.argv[1]

    f = open(file_name, 'rb')
    extractFile(f)
    f.close()
