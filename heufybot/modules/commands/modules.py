from twisted.plugin import IPlugin
from heufybot.moduleinterface import IBotModule
from heufybot.modules.commandinterface import BotCommand
from zope.interface import implements


class ModulesCommand(BotCommand):
    implements(IPlugin, IBotModule)

    name = "Modules"

    def triggers(self):
        return ["modules"]

    def execute(self, server, source, command, params, data):
        loadedModules = sorted(self.bot.moduleHandler.loadedModules.keys())
        self.bot.servers[server].outputHandler.cmdNOTICE(source, "Loaded modules: {}".format(", ".join(loadedModules)))

modulesCommand = ModulesCommand()
