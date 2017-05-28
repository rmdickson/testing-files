from fibonacci import fibonacci

def test_fib0():
    observed = fibonacci(0)
    assert observed == 1
    
def test_fib1():
    observed = fibonacci(1)
    assert observed == 1
    
def test_fib4():
    observed = fibonacci(4)
    assert observed == 5
    
def test_fib_neg():
    observed = fibonacci(-1)
    assert observed == NotImplemented