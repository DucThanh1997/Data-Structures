# Hàng đợi ưu tiên cũng có những tính chất giống như hàng đợi đó là chèn phần tử vào phía cuối và lấy ra từ phía đầu.
# Nhưng có điểm khác đó là thứ tự các phần tử trong hàng đợi ưu tiên phụ thuộc vào dộ ưu tiên của phần tử đó
# còn hàng đợi bình thường thì tuân theo tính chất FIFO (vào trước ra trước).
#
# Phần tử với độ ưu tiên cao nhất sẽ được xếp lên đầu hàng đợi và phần tử với độ ưu tiên thấp nhất sẽ được chuyển xuống cuối.
#
# Do vạy, khi bạn chèn một phần tử vào cuối hàng đợi ưu tiên, no có thể được chuyển lên đầu tiên nếu độ ưu tiên của nó là cao nhất.
# Giống như vào bệnh viện không phải ai đến trước cũng được xử lí trước mà do độ khẩn cấp của bệnh nhân

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == []

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

if __name__ == '__main__':
    myQueue = PriorityQueue()
    myQueue.insert(12)
    myQueue.insert(1)
    myQueue.insert(14)
    myQueue.insert(7)
    print(myQueue)
    while not myQueue.isEmpty():
        print(myQueue.delete())
