def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))

def descending_order(num) -> int:
  return int("".join(sorted([x for x in str(num)],reverse=True)))
