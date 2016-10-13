def bmi(weight_array, height_array,is_metric):
    bmi_result = []


    #Comparing arrays' length
    if(weight_array is None or height_array is None or (len(weight_array) != len(height_array)) or  len(height_array) == 0 or len(weight_array) == 0) :
        return ["problem with array"];

    for i in range(len(weight_array)):

        if(weight_array[i] <= 0 or height_array[i] <= 0 ):
                bmi_result.append("incorrect cell value")
                continue
        elif((is_metric and ( weight_array[i] >= 600 or height_array[i] >= 400)) or
        ((is_metric == 0 ) and ( weight_array[i] >= 1200 or height_array[i] >= 150)) ):
                bmi_result.append("incorrect cell value")
                continue
	    #calculates each value's bmi                
        if(is_metric):    
            bmi_value =float(weight_array[i])/float((height_array[i]*height_array[i])) * 10000
        else:
            bmi_value =float(weight_array[i] * 703)/float((height_array[i]*height_array[i]))

        #appends result to the return obje- bmi(array)
        if( bmi_value <= 18):
           bmi_result.append("underweight")
        elif( bmi_value < 25):
           bmi_result.append("normal")
        elif( bmi_value < 30):
           bmi_result.append("overweight")
        else:
           bmi_result.append("obese")

    return bmi_result
