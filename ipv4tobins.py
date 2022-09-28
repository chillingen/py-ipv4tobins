import math
import sys

def main():
    print("IPv4 to BIN")
    
    if len(sys.argv) > 1:
        print("BIN: {}".format(ipv4tobins(sys.argv[1])), end="")
        return

    user = input("IPv4> ")
    print("BIN: {}".format(ipv4tobins(user)), end="")
    return
    
def ipv4tobins(ipv4):
    s = ""
    for x in ipv4.split("."):
        s += i8tobins(int(x))
    
    return s
    
def i8tobins(i8):
    remainder = 0
    s = ""
    
    for x in range(7, -1, -1):
        remainder = (i8 / pow(2, x)) % 2
        remainder = math.floor(remainder)
        s += str(remainder)

    return s
    
if __name__ == "__main__":
    main()
