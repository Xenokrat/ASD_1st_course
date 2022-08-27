from linked_list import LinkedList, Node


def combine_linked_lists(l_list1: LinkedList, l_list2: LinkedList):
    """
    :param l_list1: instance of LinkedList
    :param l_list2: instance of LinkedList
    :return: LinkedList with values equal to sum of values of l_list1 and l_list2 for each node
    or None not applicable
    """
    # check if linked lists have same length, or it's empty lists
    if (not l_list1.len() == l_list2.len()) or (l_list1.len() == 0):
        return None

    node1 = l_list1.head
    node2 = l_list2.head
    res_llist = LinkedList()

    while node1 is not None:
        # adding values for new list
        new_value = node1.value + node2.value
        res_llist.add_in_tail(Node(new_value))

        node1 = node1.next
        node2 = node2.next

    return res_llist
