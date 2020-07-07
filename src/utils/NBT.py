import os
from utils import logger, Binary

class NBT:
    root = []
    TAG_END = 0
    TAG_BYTE = 1
    TAG_SHORT = 2
    TAG_INT = 3
    TAG_LONG = 4
    TAG_FLOAT = 5
    TAG_DOUBLE = 6
    TAG_BYTE_ARRAY = 7
    TAG_STRING = 8
    TAG_LIST = 9
    TAG_COMPOUND = 10
    TAG_INT_ARRAY = 11
    TAG_LONG_ARRAY = 12

    def loadFile(filename):
        if os.path.isfile(filename):
            fp = open(filename, encoding="latin-1")
        else:
            print("First parameter must be a filename")
            return False
        bname = os.path.splitext(os.path.basename(filename))[0]
        if bname == 'level':
            version = Binary.readLInt(fp.read(4))
            lenght = Binary.readLInt(fp.read(4))
        elif(bname == 'entities'):
            fp.read(12)
        PyNBT.traverseTag(fp, NBT.root)
        return next(reversed(NBT.root), None)
            
    def traverseTag(fp, tree):
        tagType = NBT.readType(fp, NBT.TAG_BYTE)
        if tagType == NBT.TAG_END:
            return False
        else:
            tagName = NBT.readType(fp, NBT.TAG_STRING)
            tagData = NBT.readType(fp, tagType)
            tree = []
            tree.append({'type': tagType, 'name': tagName, 'value': tagData})
            return True
        
    def readType(fp, tagType):
        if tagType == NBT.TAG_BYTE:
            return Binary.readByte(fp.read(1))
        elif tagType == NBT.TAG_SHORT:
            return Binary.readLShort(fp.read(2))
        elif tagType == NBT.TAG_INT:
            return Binary.readLInt(fp.read(4))
        elif tagType == NBT.TAG_LONG:
            return Binary.readLLong(fp.read(8))
        elif tagType == NBT.TAG_FLOAT:
            return Binary.readLFloat(fp.read(4))
        elif tagType == NBT.TAG_DOUBLE:
            return Binary.readLDouble(fp.read(8))
        elif tagType == NBT.TAG_BYTE_ARRAY:
            arrayLength = NBT.readType(fp, NBT.TAG_INT)
            arr = []
            i = 0
            while i < arrayLength:
                i += 1
                arr = NBT.readType(fp, NBT.TAG_BYTE)
                return arr
        elif tagType == NBT.TAG_STRING:
            stringLength = NBT.readType(fp, NBT.TAG_SHORT)
            if not stringLength:
                return ""
            string = fp.read(stringLength)
            return string
        elif tagType == NBT.TAG_LIST:
            tagID = NBT.readType(fp, NBT.TAG_BYTE)
            listLength = NBT.readType(fp, NBT.TAG_INT)
            list = {'type': tagID, 'value': []}
            i = 0
            while i < listLength:
                i += 1
                list["value"].append(NBT.readType(fp, tagID))
            return list
        elif tagType == NBT.TAG_COMPOUND:
            tree = []
            while traverseTag(fp, tree): pass
            return tree
        elif tagType == NBT.TAG_INT_ARRAY:
            pass
        elif tagType == NBT.TAG_LONG_ARRAY:
            pass

