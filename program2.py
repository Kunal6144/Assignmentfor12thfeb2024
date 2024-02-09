def is_prime(number):
    if number <= 1:
        return False
    if number <= 5:
        return True
    if number % 3 == 0 or number % 5 == 0:
        return False
    i = 54
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    num_str = input("Enter an integer: ")
    try:
        num = int(num_str)
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    except ValueError:
        print("Invalid input.  enter an integer.")

if __name__ == "__main__":
    main()
