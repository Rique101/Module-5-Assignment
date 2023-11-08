from node import *

def main():
    Assignment()

def Assignment():
    #Question 1
    head = node(2, None)
    head = node("=", head)
    head = node(1, head)
    head = node("+", head)
    head = node(1,head)

    #Question 2
    operator = head

    #Question 3
    operator = operator.getLink()

    #Question 4
    result = head

    #Question 5
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()

    #Question 6
    operator.setData("-")
    result.setData(0)

    #Question 7
    operator.setData("*")
    result.setData(1)
    
    #Question 8
    operator.setData("/")

    #Question 9
    head.setData(7)
    result.setData(7)

    #Question 10
    operator = operator.getLink()

    #Question 11
    head.removeNodeAfter()
    operator.removeNodeAfter()

    #Question 12
    print(f"Head contains {node.listlength(head)} nodes")
    print(f"Operator contains {node.listlength(operator)} nodes")
    print(f"Result contains {node.listlength(result)} node")

    #Question 13
    print("Head contains character", node.listSearch(head, 1).getData())
    print("Operator contains character", node.listSearch(operator, 1).getData())
    if(node.listSearch(result, 1) != None):
        print("Result contains character:", node.listSearch(result, 1).getData())
    else:
        print("Result doesn\'t contain character 1.")
    
    #Question 14
    copy = node.listCopyWithTail(head)

    #Question 15
    print("Copy[0] contains", node.listlength(copy[0]), "nodes")
    print("Copy[1] contains", node.listlength(copy[1]), "node")

    #Question 16
    print("Copy[0] contains character", node.listSearch(copy[0], 1).getData())
    if(node.listSearch(copy[1], 1) != None):
        print("Copy[1] contains character:", node.listSearch(copy[1], 1).getData())
    else:
        print("Copy[1] doesn\'t contain character 1.")
if __name__ == "__main__":
    main()