from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from p2pTCP.htcp.punchProtocol import ConnectionBroker


import struct, socket, time, logging

class MessageReceived(ConnectionBroker):
    
    def __init__(self):
        pass
        
reactor.listenUDP(6060, MessageReceived())
reactor.run()
