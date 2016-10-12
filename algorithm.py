def bmi(weight_array, height_array):
    bmi = []

    if(len(weight_array) != len(height_array)):
        return bmi;


    for i in range(len(weight_array)):
        if(weight_array[i] <= 0 or weight_array[i] >= 700):
            bmi.append("incorrect weight")
            continue

        if(height_array[i] <= 0 or height_array[i] >= 350):
            bmi.append("incorrect height")
            continue

        bmi_value =float(weight_array[i])/float((height_array[i]*height_array[i])) * 10000
        #        bmi.append(bmi_value)
        if( bmi_value <= 18):
           bmi.append("underweight")
        elif( bmi_value < 25):
           bmi.append("normal")
        elif( bmi_value < 30):
           bmi.append("overweight")
        else:
           bmi.append("obese")

    return bmi