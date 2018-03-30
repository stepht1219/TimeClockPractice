#tv.py
#Stephanie Tattrie
#Create Date 

class tv:
    def __init__(self, channel = 5, volume = 2, power = 0):
        self.channel = channel
        self.power = power
        self.volume = volume
    
    def getChannel(self):
        return self.channel

    def getVolume(self):
        return self.volume

    def setChannel(self,channel):
        self.channel = channel
        return self.channel

    def setVolume(self,volume):
        self.volume = volume
        return self.volume
    
    def channelUp(self):
        self.channel = self.channel + 1
        return self.channel

    def channelDown(self):
        self.channel = self.channel - 1
        return self.channel

    def volumeUp(self):
        self.volume = self.volume + 1
        return self.volume

    def volumeDown(self):
        self.volume = self.volume - 1
        return self.volume

    def getPower(self):
        return "TV is off"

    def setPower(self, power):
        self.power = power
        return self.power 
