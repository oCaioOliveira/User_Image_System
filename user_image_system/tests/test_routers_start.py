from routers.start import welcome


def test_start():
    response = welcome()
    assert response == 'Welcome to the User Image System! For further information, read the documentation in /docs or /redoc.'
