def calculate_bmi(weight, height_cm): #calculates bmi and returns the category

    height_m=height_cm/100 # convert height to meters
    bmi=weight/(height_m**2) # finding bmi using formula
    return round(bmi,2)


def get_category(bmi): #uses rule-based classification logic

    if(bmi<18.50):
        return "Underweight"
    elif(18.5<=bmi<=24.9):
        return "Normal Weight"
    elif(25.0<=bmi<=29.9):
        return "Overweight"
    else:
        return "Obese"
    

def find():

    print("\n-----------BMI Classifier:---------")
    try: #user inputs via CLI
        weight=float(input("\nEnter weight in kilograms(eg: 70kg) : "))
        height=float(input("Enter height in centimeters(eg: 160cm): "))
        if(weight<=0 or height<=0):
            print("\n")
            print("ERROR!!! Weight and Height must be positive numbers.")
            print("\n")
            return
        #AI logic
        bmi_score=calculate_bmi(weight,height)
        category=get_category(bmi_score)
        #output
        print(f"\n---Result:---")
        print("\n")
        print(f"Calculated BMI: {bmi_score}")
        print(f"Health Cateogry: {category}")
        print("\n")
        print(f"-----------------")
    except ValueError:
        print("\n")
        print("ERROR!!! Please enter valid numerical value.")  
        print("\n")

if __name__=="__main__":
    find()
         

