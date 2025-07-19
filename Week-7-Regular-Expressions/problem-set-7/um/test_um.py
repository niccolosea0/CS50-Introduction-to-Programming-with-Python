from um import count

def test_one_um():
    assert count("Hello, um, world") == 1
    assert count("um, hello") == 1

def test_two_um():
    assert count("um, how are you um doing?") == 2
    assert count("Um, how do you do, um?") == 2

def test_without_um():
    assert count("hello") == 0

def test_with_um_in_word():
    assert count("Mum hello, um how is dad? mummy is okay yea? um and love you") == 2
