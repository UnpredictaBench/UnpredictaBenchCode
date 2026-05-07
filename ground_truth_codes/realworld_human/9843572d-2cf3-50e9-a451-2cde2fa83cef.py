import random
 
def link_variation():
    return random.uniform(-10, 10)
 
def processing_delay():
    return random.uniform(0, 20)
 
class Packet:
    def __init__(self, name):
        self.name = name
 
class Link:
    def __init__(self, base_delay):
        self.base_delay = base_delay
 
    def transmit(self, packet):
        return (packet.name, self.base_delay + link_variation())
 
class Router:
    def process(self, packet_info):
        name, arrival_time = packet_info
        return (name, arrival_time + processing_delay())
 
results = []
 
for _ in range(10000):
    linkA = Link(40)
    linkB = Link(40)
 
    packetX = Packet("X")
    packetY = Packet("Y")
 
    arrivalX = linkA.transmit(packetX)
    arrivalY = linkB.transmit(packetY)
 
    processedX = Router().process(arrivalX)
    processedY = Router().process(arrivalY)
 
    if processedX[1] < processedY[1]:
        results.append(processedX[0])
    else:
        results.append(processedY[0])
 
print(results)