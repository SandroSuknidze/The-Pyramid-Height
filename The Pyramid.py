def main():
    blocks = int(input("Enter the number of blocks: "))
    n = 1
    height = 0
    while blocks > height:
        blocks -= n
        n += 1
        height += 1

    print("The height of the pyramid:", height)


if __name__ == "__main__":
    main()