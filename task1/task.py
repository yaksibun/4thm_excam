def qaytar(lst):
  res = []  
  for i in lst:
    count = 0
    for j in lst[1:]:
      if i > j:
        count += 1
    res.append(count)
    print(f"{i} dan kichik {count} ta ")
  return res

lst = [6, 5, 4, 8]
print(qaytar(lst))