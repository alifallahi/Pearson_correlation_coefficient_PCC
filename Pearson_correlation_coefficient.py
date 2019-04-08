
def average_calculator(list_input):
    temp_sum = 0

    len_list_input = len(list_input)

    for x in list_input:
        temp_sum = temp_sum + x

    average_list_input = temp_sum / len_list_input
    ###print("average of the input is", average_list_input)
    return average_list_input


def find_corated_items(array1, array2):
    temp_corated = []
    
    for x1 in range(0, len(array1)):
        if array1[x1] > 0 and  array2[x1] >0:
            temp_corated.append(x1)

    ###print("corated items are: " , temp_corated)        
    return temp_corated
        

def pcc(item1, item2):
#Pearson correlation coefficient calculator
    pcc_result = 0
    average_item1 = average_calculator(item1)
    average_item2 = average_calculator(item2)
    corated_items = find_corated_items(item1, item2)

    temp_pcc_numerator = 0
    temp_pcc_denumerator1 = 0
    temp_pcc_denumerator2 = 0
    temp_pcc_denumerator_total = 0

    for x2 in corated_items:
        temp_pcc_numerator = temp_pcc_numerator +(item1[x2] - average_item1) * (item2[x2] - average_item2)
        temp_pcc_denumerator1 = temp_pcc_denumerator1+ ((item1[x2] - average_item1)**2)
        temp_pcc_denumerator2 = temp_pcc_denumerator2 + ((item2[x2] - average_item2)**2)
        
    temp_pcc_denumerator_total = (temp_pcc_denumerator1 * temp_pcc_denumerator2)**0.5
    pcc_result = temp_pcc_numerator / temp_pcc_denumerator_total
    
    return pcc_result
        
        

    

a = [1,2,3,3,3,5,4]
b = [1,0,4,1,2,1,1]
print(pcc(a,b))
