class Peer:
    def __init__(self, name):
        self.name = name
        self.peers = []

    def add_peer(self, peer):
        self.peers.append(peer)
        peer.peers.append(self)

    def send_message(self, message):
        print(f"{self.name} sent message: {message}")
        for peer in self.peers:
            peer.receive_message(self, message)

    def receive_message(self, sender, message):
        print(f"{self.name} received message from {sender.name}: {message}")