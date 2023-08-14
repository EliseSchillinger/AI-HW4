from cgi import test
import heapq
path = []
test_list = []

test_list.append((6, [1,2,3,4,5]))
test_list.append((5, [1,2,3,4,5]))
test_list.append((3, [1,2,3,4,5]))


heapq.heapify(test_list)

path = heapq.heappop(test_list)
path = path[1]
frontier = []

a = 1
# decrement
a -= 1

test_tuple = ()

test_tuple = (0,[])
test_tuple2 = (1, [2,3,4])
frontier.append(test_tuple)
frontier.append(test_tuple2)

abc = frontier[1]
print(abc)




