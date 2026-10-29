list1=['aravind','aparna']
print("The original list:\n"+str(list1))
res=[ord(ele)for sub in list1 for ele in sub]
print("The ASCII list  is:\n"+str(res))  
