def qaytar(text):
  lst = []
  lst1 = []
  for i in text.split():
    if i.isdigit():
     lst.append(i)
  lst1 = sorted(lst, key=int)
  print(lst)  
  
  if lst == lst1:
    return True
  else:
    return False


text = input("Text: ")

print(qaytar(text))



