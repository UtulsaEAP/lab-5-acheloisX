def kilo_to_pounds(kilos):
    return (kilos * 2.204)
if __name__ == '__main__':
    kilos = float(input("Enter weight in kilos: "))
    pounds = kilos * 2.204
        
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.3f} lbs')