original_list=[10,20,30,50,60,70]
modified_list=[40,20,30,50,60,70]
missing_element = []
for i in range(len(original_list)):
    if original_list[i]!= modified_list[i]:
        missing_element.append(original_list[i])

print("The missing element is",missing_element)