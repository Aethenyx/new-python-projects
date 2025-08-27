def main():
    while True:
        print("1. Addition")
        print("1. Subtracrion")
        print("1. Multiplication")
        print("1. Division")

        choice = input("Enter your choice 1 - 4 (q to quit): ")

        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a number: "))
        if choice == '1':
            print(num1 + num2)
        elif choice == '2':
            print(num1 - num2)
        elif choice == '3':
            print(num1 * num2)
        elif choice == '4':
            print(num1 / num2)
        elif choice == 'q':
            break
        elif choice == 'Q':
            break
        else:
            print("Plese enter a valid numebr.")
main()