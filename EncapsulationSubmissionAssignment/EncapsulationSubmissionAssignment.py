

#create class with protected and private attributes
class protectedData:
    def __init__(self):
        self._protectedID = 55
        self.__privateID = 13

#create method to get private attribute
    def getPrivateData(self):
        print(self.__privateID)

#create method to set private attribute
    def setPrivateData(self, data):
        self.__privateID = data


#create protectedData obj called protObj
protObj = protectedData()
#print unchanged protected ID
print(protObj._protectedID)
#change protObj to 1155
protObj._protectedID = 1155
#print changed protectedID
print(protObj._protectedID)


#create protectedData obj called privObj
privObj = protectedData()
#get private Id value using method getPrivateData
privObj.getPrivateData()
#set private Id value to 1113 using method setPrivateData
privObj.setPrivateData(1113)
#get new private ID value using method getPrivateData
privObj.getPrivateData()
