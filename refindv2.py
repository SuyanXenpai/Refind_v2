#Introduction
print("Welcome to the Finder. ")
print("Here, you just need to simply paste your contents and press Ctrl+D to save it")
print("After that, please follow the instructions to find or replace a text within the contents")
print("----------------------------------------------")


#Starting Phase 1
#Inputting the content
print("Enter/Paste your content. Ctrl-D to save it.")
contents = []
while True:
  try:
    line = input()
  except EOFError:
    break
  contents.append(line)
print("----------------------------------------------")
 

#Defining a function to make parts of contents go uppercase
def uppercase(x):
  for ele in range(len(contents)):
    list1 = contents[ele].split()
    #print(list1)

    for i in range(len(list1)):
      if list1[i] == x:
        list1[i] = list1[i].upper()
    #print(list1)
    contents[ele] = " ".join(list1)
    #print(contents[0] + "\n")
  print("\n".join(contents))






#Starting Phase 2
input("Press any key to continue...")
print("----------------------------------------------")


dec = int(input("Press 1 to find a text and 2 to replace: "))
print("----------------------------------------------")


#Starting sub-phase FIND
if (dec==1):
  print("So, you have choosen to FIND a text")
  find = str(input("Enter the text you want to find: "))
  item = list(filter(lambda x: find in x, contents)) 
  print("All the texts referenced with given item are: \n" + str(item))
  print("\ \ \ ")
  print("The hightlighted text version is: ")
  uppercase(find)


#Starting sub-phase REPLACE
elif(dec==2):
  print("So, you have choosen to REPLACE a text")
  r1 = str(input("Enter the item you want to replace: "))
  r2 = str(input("Enter the new item to be placed in the position: "))
  print("/ / / / /")

  if any(r1 in ele for ele in contents):
    print("Replacing... \n" + r1 + "-->" + r2)
    contents = [item.replace(r1 , r2) for item in contents]
    print("So, the replaced text result is: \n" + "\n".join(contents))
      
  else:
    print("Unknown item detected")


else:
  print("INVALID keyword detected. Choose the number 1 or 2")

print("----------------------------------------------")



  

