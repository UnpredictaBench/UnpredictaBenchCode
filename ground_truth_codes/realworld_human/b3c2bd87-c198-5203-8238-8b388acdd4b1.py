import random

def transmission_variation():
    return random.uniform(-10, 10)

def switching_delay():
    return random.uniform(0, 10)

def server_delay():
    return random.uniform(0, 10)

class Packet:
    def __init__(self, name):
        self.name = name

class Channel:
    def __init__(self, base_delay):
        self.base_delay = base_delay

    def deliver(self, packet):
        return (packet.name, self.base_delay + transmission_variation())

class Switch:
    def forward(self, packet_info):
        name, arrival_time = packet_info
        return (name, arrival_time + switching_delay())

class Server:
    def receive(self, packet_info):
        name, arrival_time = packet_info
        return (name, arrival_time + server_delay())

results = []

for _ in range(10000):
    channel1 = Channel(20)
    channel2 = Channel(35)
    channel3 = Channel(25)
    channel4 = Channel(30)

    packets = [Packet("P1"), Packet("P2"), Packet("P3"), Packet("P4")]

    arrivals = [
        channel1.deliver(packets[0]),
        channel2.deliver(packets[1]),
        channel3.deliver(packets[2]),
        channel4.deliver(packets[3]),
    ]

    forwarded = [Switch().forward(x) for x in arrivals]
    received = [Server().receive(x) for x in forwarded]

    first_packet = min(received, key=lambda x: x[1])
    results.append(first_packet[0])

print(results)