def find_two_transactions(amounts:list, target:int) -> list:
    """
      input: Given a list of transaction amounts and a target amount, 
      return: the indices of two transactions whose amounts sum to the target.
    """
    seen = {}
    for index, amount in enumerate(amounts):
        needed = target - amount 
        if needed in seen:
            return [seen[needed], index]
        seen[amount] = index
        print(seen)
        # print(f"{index}, {seen[amount]}")
   
    return None

amounts = [120, 250, 80, 420]
target = 330

print(find_two_transactions(amounts, target))