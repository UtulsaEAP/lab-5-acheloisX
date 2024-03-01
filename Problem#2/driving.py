#Nhi Tran
def driving_cost(miles_per_gallon, dollars_per_gallon, 
    miles_driven=10.0):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon
        
if __name__ == '__main__':
    
    miles = float(input("Enter miles: "))
    dollars = float(input("ENter dollars per gallon: "))

    price = driving_cost(miles, dollars) 
    print(f'{price:.2f}')
    print(f'{price * 5:.2f}')
    print(f'{price * 40:.2f}')