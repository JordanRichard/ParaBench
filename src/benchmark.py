################################################################################
#   benchmark.py              Last Updated: 22 March 2022
#
#   Jordan Richard
#
#   This program is intended to serve as a benchmarking
#   application using mersenne prime searching techniques
#
################################################################################
import platform
import wmi
import psutil

sys = platform.uname()
c = wmi.WMI()
winSys = c.Win32_ComputerSystem()[0]

mode1 = "Integer Mode"
mode2 = "Floating-Point Mode"

#Lucas -Lehmer function testing up to the n'th power mersenne primes printing as it goes
def ll_series (p):
    ll_list=[4]

    for i in range(1, p+1):
        ll_list.append((ll_list[i-1]**2 - 2) % (2**p-1))
        print(ll_list[i])                           #CHANGE TO PRINT LINE BY LINE
        print("\n")
    return ll_list

# Primality test 2^p - 1
# Return true if 2^p - 1 is prime
def lucas_lehmer_test(p: int) -> bool:
    """
    >>> lucas_lehmer_test(p=7)
    True

    >>> lucas_lehmer_test(p=11)
    False

    # M_11 = 2^11 - 1 = 2047 = 23 * 89
    """

    if p < 2:
        raise ValueError("p should not be less than 2!")
    elif p == 2:
        return True

    s = 4
    M = (1 << p) - 1
    for i in range(p - 2):
        s = ((s * s) - 2) % M
    return s == 0


if __name__ == "__main__":
    print(lucas_lehmer_test(7))
    print(lucas_lehmer_test(11))




print("_________________________________________________________________________________")
print("------------------------------System Information---------------------------------")
print(f"\tOS: {sys.system} {sys.release} ") #
print(f"\tMachine Name: {sys.node}")
print(f"\tVersion: {sys.version}")
print(f"\tCPU: {sys.processor}")
print("\tNumber of Cores: " + str(psutil.cpu_count()))
print(f"\tRAM: {psutil.virtual_memory()}")
print("---------------------------------------------------------------------------------")
print("Welcome to ParaBench! Please select what benchmarking mode you would like to use." + '\n')
print("[1] -> " + mode1 + '\n' + "[2] -> " + mode2 + "\n[3] -> Exit")
print("_________________________________________________________________________________")

modeSelect = 0

while modeSelect != 3:                                                          #Main loop to keep program running while waiting for a user decision. Kills program on [3]
    modeSelect = int(input())                                                   #TODO - Use selections later on to call benchmarking functions
    if modeSelect == 1:
        print("User Selected " + mode1)
        order = int(input("Enter what order prime to find\n"))

        if lucas_lehmer_test(order):
            print(str(order) + "Is a mersenne prime")
        else:
            print(str(order) + "Is NOT a mersenne prime")

    if modeSelect == 2:
        print("User Selected " + mode2)


#def lehmer(p):
#    M = 2**p - 1
#    s = 4
#    for i in range(p-2) :
#        s = (s*s - 2) % M
#    return s == 0
