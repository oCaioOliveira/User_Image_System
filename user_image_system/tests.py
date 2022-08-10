from tests.test_crud_user import test_update_user
from tests.test_routers_health import test_alive, test_live, test_ready
from tests.test_routers_start import test_start

try:
    test_alive()
    print('Passed!')
except:
    print('Failed!')

try:
    test_live()
    print('Passed!')
except:
    print('Failed!')

try:
    test_ready()
    print('Passed!')
except:
    print('Failed!')

try:
    test_start()
    print('Passed!')
except:
    print('Failed!')

test_update_user()
