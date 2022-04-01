################################################################################
#   benchmark.py              Last Updated: 29 March 2022
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
from time import perf_counter
from concurrent.futures import ProcessPoolExecutor


#from pyJoules.energy_meter import measure_energy

sys = platform.uname()
c = wmi.WMI()
winSys = c.Win32_ComputerSystem()[0]

mode1 = "Integer Mode"
mode2 = "Floating-Point Mode"

def lehmer(p: int) -> bool:

    s = 4
    M = (1 << p) - 1
    for i in range(p - 2):
        s = ((s * s) - 2) % M
    return s == 0




if __name__ == '__main__':
    #Initial printout of system information and menu screen schowing benchamrking options
    print("_________________________________________________________________________________")
    print("------------------------------System Information---------------------------------")
    print(f"\tOS: {sys.system} {sys.release} ") #
    print(f"\tMachine Name: {sys.node}")
    print(f"\tVersion: {sys.version}")
    print(f"\tCPU: {sys.processor}")
    print("\tNumber of Cores: " + str(psutil.cpu_count()))
    print(f"\tRAM: {psutil.virtual_memory()}")
    print("---------------------------------------------------------------------------------")


    modeSelect = 0;
    print("Welcome to ParaBench! Please select what benchmarking mode you would like to use." + '\n')
    modeSelect = int(input("[1] -> " + mode1 + '\n' + "[2] -> " + mode2
        + "\n[9] -> Exit\n_________________________________________________________________________________\n"))


    #User selects Integer benchmarking mode
    if modeSelect == 1:
        print("User Selected " + mode1)

        #Printout of selection for order of magnitude
        print("[1] -> First 1x10^2 Primes\n" +  "[2] -> First 1x10^3 Primes\n"
            +"[3] -> First 1x10^4 Primes\n" + "[4] -> First 1x10^5 Primes\n" + "[5] -> First 1x10^6 Primes\n")
        mersenneOrder = int(input("Please Select an option\n"))


        if mersenneOrder == 1:
            print("Starting Benchmark...")
            with ProcessPoolExecutor(15) as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,100)):
                    print(result)
                timeStop = perf_counter()

                print("1E2 Benchmark Complete in ",timeStop-timeStart)


        if mersenneOrder == 2:
            print("Starting Benchmark...")
            with ProcessPoolExecutor(15) as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,1000)):
                    print(result)
                timeStop = perf_counter()
                print("1E3 Benchmark Complete!!", timeStop-timeStart)


        if mersenneOrder == 3:
            print("Starting Benchmark...")
            with ProcessPoolExecutor() as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,10000)):
                    print(result)
                timeStop = perf_counter()
                print("1E4 Benchmark Complete!!", timeStop-timeStart)


        if mersenneOrder == 4:
            print("Starting Benchmark...")
            with ProcessPoolExecutor(15) as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,100000)):
                    print(result)
                timeStop = perf_counter()
                print("1E5 Benchmark Complete!!", timeStop-timeStart)


        if mersenneOrder == 5:
            print("Starting Benchmark...")
            with ProcessPoolExecutor(15) as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,1000000)):
                    print(result)
                timeStop = perf_counter()
                print("1E6 Benchmark Complete!!", timeStop-timeStart)

            #Single-threaded test (DEPRECATED)
            #for x in range(2,1000000):
            #    if lehmer(x):
            #        print(x)


    if modeSelect == 2:                                                         # TODO: User selects floating point mode
        print("User Selected " + mode2)
