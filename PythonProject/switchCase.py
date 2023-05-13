def age(num):
    match num:
        case 0:
            print("zero")
        case 1:
            print("one")
        case 2:
            print("two")


def relation(name):
    match name:
        case "Krishna":
            print("Husband")
        case "Sridhar":
            print("Baaps")
        case "Usha":
            print("Amman Thaayi")



if __name__ == '__main__':
    age(2)
    relation("Usha")