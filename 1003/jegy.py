import random

def main():
    print("Véletlen jegy generátor")
    print(f"Az én félévi jegyem: {random.randrange(1, 5)}") # [1,5[
    print(f"Az én félévi jegyem: {random.randint(1, 5)}")   # [1,5[

if __name__ == "__main__":
    main()