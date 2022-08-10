from datetime import datetime

from routers.health import alive, live, ready


def test_live():
    response = live()
    assert response == 'LIVE'


def test_ready():
    response = ready()
    assert response == 'READY'


def test_alive():
    response = alive()
    assert response == {'timestamp': datetime.now()}
