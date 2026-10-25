def get_duplicates(values:list) -> int:
   """
    Time: O(n + dlog d)
    Where d is the number of distinct duplicated IDs due to sorting
    Without sorting expected time is O(n)
   """ 
   seen = set()
   duplicates = set()

   for value in values:
      if value in seen:
         duplicates.add(value)
      else: 
         seen.add(value)
   return sorted(duplicates)

customer_ids = [101, 205, 101, 309, 205, 410]
print(get_duplicates(customer_ids))