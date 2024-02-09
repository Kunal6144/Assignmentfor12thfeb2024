def main():
    numbers = []

    # Keep communicating with the user for numbers until they input an empty string
    while True:
        num_str = input("Enter a number : ")
        if num_str == '':
            break
        try:
            num = float(num_str)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Sort the numbers in descending order
    numbers.sort(reverse=True)

    # Print the five greatest numbers
    print("five greatest numbers are:")
    for num in numbers[:5]:
        print(num)

if __name__ == "__main__":
    main()
