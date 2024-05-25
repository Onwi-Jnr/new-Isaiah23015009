def remove_duplicates(texts):
    item = [] 
    for x in texts:
        if x not in item:
            item.append(x)  
    return item
store = input("Pls enter your items  ").split()
update_list = remove_duplicates(store)
print("new_ list:", update_list)
