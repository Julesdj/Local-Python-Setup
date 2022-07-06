def hello() :
    print("Hello there!")

hello()

def pack(item, container, label):
    return [item, container, label]

print(pack("sneakers", "box", "sold"))


def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")


eat_lunch([])
eat_lunch(["pizza"])
eat_lunch(["snacks","burger","peach"])