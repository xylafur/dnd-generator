class TestFailure(Exception):pass
class TestIncomplete(Exception):pass

def test_assert(exp):
    if not exp:
        raise TestFailure()


