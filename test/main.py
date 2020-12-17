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
        yield datum(types[random.randint(0, 2)], i)

x = dripper()
done = False

while True:
    if done:
        print("exiting")
        break
    print("{")
    try:
        for i in range(random.randint(1, 5)):
            q.append(next(x))
    except Exception as e:
        print("done set to true")
        done = True

    while True:
        print("  [")
        event = None
        if len(q) > 0:
            event = q.pop(0)
        else:
            print("    queue empty.")
            print("  ]")
            break

        if event == None:
            print("    Invalid event")
        elif event.the_type == "A":
            print("    Type A with info = {}".format(event.the_info))
        elif event.the_type == "B":
            print("    Type B with info = {}".format(event.the_info))
        elif event.the_type == "C":
            print("    Type C with info = {}".format(event.the_info))
        else:
            print("    Invalid type")

        print("  ]")

    print("}\n")
