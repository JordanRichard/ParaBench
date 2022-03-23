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
    if modeSelect == 2:
        print("User Selected " + mode2)
