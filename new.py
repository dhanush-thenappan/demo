def main(user):
    for i in range(0, 10):
        print(f'{i+1}. Hello, {user}')

if __name__ == '__main__':
    name = input("Enter your user name: ")
    main(name)
