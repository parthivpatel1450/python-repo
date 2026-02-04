
class Network:
    def connectivity(self):
        return "Network connects"

class Network_5G(Network):
    def fast_connectivity(self):
        return "5G Network provides superfast connectivity"

class Network_5G_Airtel(Network_5G):
    def fast_and_stable_connectivity(self):
        return "Airtel 5G network is fast and remains stable"    

network_object = Network_5G_Airtel()
print(network_object.connectivity())        
print(network_object.fast_connectivity())   
print(network_object.fast_and_stable_connectivity())   