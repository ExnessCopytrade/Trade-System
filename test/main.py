import random

class datum():
    def __init__(self, type, info):
        self.the_type = type
        self.the_info = info

q = []
types = ["A", "B", "C"]


def dripper():
    '''enqueues one or more until finished'''
    for i in range(20):
        q.append(datum(types[random.randint(0, 2)], i))

while True:


    while True:
        event = None
        if len(q) > 0:
            event = q.pop(0)
        else:
            print("queue empty. exiting")
            break

        if event == None:
            print("Invalid event")
        elif event.the_type == "A":
            print("Type A with info = {}".format(event.the_info))
        elif event.the_type == "B":
            print("Type B with info = {}".format(event.the_info))
        elif event.the_type == "C":
            print("Type C with info = {}".format(event.the_info))
        else:
            print("Invalid type")

    print()
