class TestFailure(Exception):pass

def test_assert(exp):
    if not exp:
        raise TestFailure()


