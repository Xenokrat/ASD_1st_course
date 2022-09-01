from stack import Stack


def is_brackets_balanced(brackets: str) -> bool:
    st = Stack()
    for bracket in brackets:
        if bracket == '(':
            st.push(bracket)

        elif (bracket == ')') and (st.size() == 0):
            return False

        else:
            st.pop()

    res = (st.size() == 0)
    return res
