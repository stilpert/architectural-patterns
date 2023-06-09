import pytest
from peer import Peer



@pytest.fixture
def peers():
    peerA = Peer("A")
    peerB = Peer("B")
    peerC = Peer("C")

    peerA.add_peer(peerB)
    peerB.add_peer(peerC)

    return peerA, peerB, peerC


def test_send_message(peers, capsys):
    peerA, peerB, peerC = peers

    peerA.send_message("sup")

    captured = capsys.readouterr().out.split('\n')

    assert "A sent message: sup" in captured
    assert "B received message from A: sup" in captured


def test_receive_message(peers, capsys):
    peerA, peerB, peerC = peers
    
    peerA.add_peer(peerC)

    peerC.send_message("the hell you want")

    captured = capsys.readouterr().out.split('\n')

    assert "C sent message: the hell you want" in captured
    assert "B received message from C: the hell you want" in captured
    assert "A received message from C: the hell you want" in captured
