from deque import Deque
from string import punctuation


def is_palindrome(text: str) -> bool:
    dq = Deque()

    # fill deque, no punctuation, no spaces
    for char in text:
        if char not in punctuation and char != ' ':
            dq.addTail(char)

    while dq.size() > 1:
        first = dq.removeFront().lower()
        last = dq.removeTail().lower()
        if first != last:
            return False

    return True