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
    
    def loadFile(self, filename):
        if os.path.isfile(filename)
            fp = open('filename')
        else:
            logger.log("warn", "First parameter must be a filename")
            return False
            bname = os.path.basename(filename)
            bname = bname[:-len(".dat")]
            if bname == level:
                version = Binary.readLInt(fp.read(4))
                lenght = Binary.readLInt(fp.read(4))
            elif(bname == entities):
                fp.read(12)
            self.traverseTag(fp, self.root)
            return self.root[-1]
            
    def traverseTag(self, fp, tree):
        tagType = self.readType(fp, self.TAG_BYTE)
        if tagType == self.TAG_END:
            return False
        else:
            tagName = self.readType(fp, self.TAG_STRING)
            tagData = self.readType(fp, tagType)
            tree = []
            tree.append({'type': tagType, 'name': tagName, 'value': tagData})
            return True
        
    def readType(fp, tagType):
        if tagType == self.TAG_BYTE:
            return Binary.readByte(fp.read(1))
        elif tagType == self.TAG_SHORT:
            return Binary.readLShort(fp.read(2))
        elif tagType == self.TAG_INT:
            return Binary.readLInt(fp.read(4))
        elif tagType == self.TAG_LONG:
            return Binary.readLLong(fp.read(8))
        elif tagType == self.TAG_FLOAT:
            return Binary.readLFloat(fp.read(4))
        elif tagType == self.TAG_DOUBLE:
            return Binary.readLDouble(fp.read(8))
        elif tagType == self.TAG_BYTE_ARRAY:
            arrayLength = self.readType(fp, self.TAG_INT)
            arr = []
            i = 0
            while i < arrayLength:
                i += 1
                arr = self.readType(fp, self.TAG_BYTE)
                return arr
        elif tagType == self.TAG_STRING:
            stringLength = self.readType(fp, self.TAG_SHORT)
            if not stringLength:
                return ""
            string = fp.read(stringLength)
            return string
        elif tagType == self.TAG_LIST:
            tagID = self.readType(fp, self.TAG_BYTE)
            listLength = self.readType(fp, self.TAG_INT)
            list = {'type': tagID, 'value': []}
            i = 0
            while i < listLength:
                i += 1
                list["value"].append(self.readType(fp, tagID))
            return list
        elif tagType == self.TAG_COMPOUND:
            tree = []
            while traverseTag(fp, tree): pass
            return tree
        
