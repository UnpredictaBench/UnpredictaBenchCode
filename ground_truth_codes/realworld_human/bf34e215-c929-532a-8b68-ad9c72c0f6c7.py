import random

def network_fluctuation():
    return random.uniform(-20, 20)

class Packet:
    def __init__(self, name):
        self.name = name

def send(packet, path):
    return (packet.name, path.get_latency())

class Path:
    def __init__(self, name, base_latency):
        self.name = name
        self.base_latency = base_latency

    def get_latency(self):
        return self.base_latency + network_fluctuation()

results = []

for _ in range(10000):
    path1 = Path("P1", 50)
    path2 = Path("P2", 70)

    packetA = Packet("A")
    packetB = Packet("B")

    resultA = send(packetA, path1)
    resultB = send(packetB, path2)

    if resultA[1] < resultB[1]:
        results.append(resultA[0])
    else:
        results.append(resultB[0])

print(results)