# Create a class and function, and list out the items in the list
class MultipleFunctions:
    def Subfields():
        subfields =["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are: ")
        for i in subfields:
            print (i)


    # Create a function that checks whether the given number is Odd or Even
    def check_odd_even():
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            print (number," is an ", "Even number")
        else:
            print (number,"is an ","Odd number")
        
    # Create a function that tells elegibility of marriage for male and female according to thei

    def Eligible():
            valid_responses=["Male","Female"]
            Gender = str(input("Please select your gender: "))
            if Gender not in valid_responses:
                print("Invalid input. Please enter Male or Female. Rerun the function")
                return
            else:
                print(Gender)
            Age = int(input("Please select your age: "))
            if Gender=="Male": 
                if Age>=21:
                    print("Eligible for marriage")
                else:
                    print("Not eligible for marriage")
            elif Gender=="Female":
                if Age>=18:
                    print("Eligible for marriage")
                else:
                    print("Not eligible for marriage")

    # calculate the percentage of your 10th mark
    def Findpercent():
        Sub1Mark=int(input("Enter your marks in Subject 1:"))
        Sub2Mark=int(input("Enter your marks in Subject 2:"))
        Sub3Mark=int(input("Enter your marks in Subject 3:"))
        Sub4Mark=int(input("Enter your marks in Subject 4:"))
        Sub5Mark=int(input("Enter your marks in Subject 5:"))
        Total=Sub1Mark+Sub2Mark+Sub3Mark+Sub4Mark+Sub5Mark
        percentage=float(Total/5)
        print("Percentage: ",percentage)

    #print area and perimeter of triangle using class and functions
    def triangle():
        height=float(input("Enter the height of the triangle:"))
        breadth=float(input("Enter the breadth of the triangle:"))
        print(height)
        print(breadth)
        print("Area formula: (height * breadth)/2")
        print("Area of the triangle:",height*breadth/2)
        slope1=float(input("Enter the slope1 of the triangle:"))
        slope2=float(input("Enter the slope2 of the triangle:"))
        print(slope1)
        print(slope2)
        print("Perimeter formula: Slope1+Slope2+Breadth")
        print("Perimeter of Triangle:",slope1+slope2+breadth)


MultipleFunctions.Findpercent()
