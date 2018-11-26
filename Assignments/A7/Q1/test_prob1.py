import problem1

def test_factor():
    assert problem1.smallest_factor(1)==1, "failed on 1"
    assert problem1.smallest_factor(2)==2, "failed on even prime number"
    assert problem1.smallest_factor(3)==3, "failed on smallest odd prime number"
    assert problem1.smallest_factor(4)==2, "failed on smallest square number other than one"
    assert problem1.smallest_factor(6)==2, "failed with factor of two prime factors, of which one is even"
    assert problem1.smallest_factor(15)==3, "failed with factor of two prime factors, both of which are odd"

