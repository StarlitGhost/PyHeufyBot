from twisted.words.protocols import irc
from twisted.internet import reactor, protocol

class PyHeufyBot(irc.IRCClient):
    self.nickname = None
    self.username = None
    self.realname = None