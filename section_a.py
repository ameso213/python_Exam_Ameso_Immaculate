
#ai)
def calculate_grade(percentage):    
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    elif 50 <= percentage < 60:
        return 'E'
    else:
        return 'Fail'

def main():
    try:
        percentage = float(input("Enter the percentage grade: "))
        if 0 <= percentage <= 100:
            grade = calculate_grade(percentage)
            print("The corresponding grade is:", grade)
        else:
            print("Percentage grade must be between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "_main_":
    main()
    
    
    
# a(ii)
# convert to and from celcius to fahrenheit
def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert temperature from Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def main():
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Check if this script is being run directly
if __name__ == "_main_":
    main() 
    
    
    
       
#b ii)
def sum_list(numbers):
      numbers = [9, 2, 3, 5, 8]
      sum = 9+2+3+5+8       
result = sum_list([])
print(result)



   
#bi)
def area_of_a_triangle(base, height):
    area= (1/2) * base * height

def main():
    base = 2
    height = 3

    # Calculate the area of the triangle
    area = area_of_a_triangle(base, height)
    print("The area of the triangle with base{base} and height {height} is:, area")

if __name__ == "_main_":
    main()
 