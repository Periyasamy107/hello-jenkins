import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python hello.py <number1> <number2>")
        sys.exit(1)
    
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])

    # Your script logic here
    print("The first number is:", n1)
    print("The second number is:", n2)

    def mul(a,b):
        return a * b 

    output = mul(n1,n2)

    print(output)

if __name__ == "__main__":
    main()
