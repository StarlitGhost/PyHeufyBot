from pyheufybot.message import IRCMessage
from pyheufybot.serverinfo import ServerInfo
from pyheufybot.heufybot import HeufyBot

class Module(object):
    def __init__(self):
        self.trigger = ""
        self.messageTypes = []
        self.helpText = "No help available for this module"

    def excecute(self, message=IRCMessage, serverInfo=ServerInfo):
        pass

    def onModuleLoaded(self):
        pass

    def onModuleUnloaded(self):
        pass

class ModuleInterface(object):
    def __init__(self, bot=HeufyBot):
        self.bot = bot
        self.modules = []

    def loadModule(self, moduleName):
        pass

    def unloadModule(self, moduleName):
        pass

    def shouldExecute(self, module=Module, message=IRCMessage):
        pass

    def handleMessage(self, message=IRCMessage):
        pass
