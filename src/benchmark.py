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
from datetime import datetime


sys = platform.uname()
c = wmi.WMI()
winSys = c.Win32_ComputerSystem()[0]

def lehmer(p: int) -> bool:

    s = 4
    M = (1 << p) - 1
    for i in range(p - 2):
        s = ((s * s) - 2) % M
    #return s == 0
        if s == 0:
            return p

#Log results and save to file
def logging():
    textfile = open("log "+ str(datetime.today().strftime("%d-%b-%y,%H.%M.%S"))
        + str(datetime.today().strftime("%H.%M.%S")) +".txt","w")
    textfile.write("------------------------------System Information---------------------------------\n")
    textfile.write(f"\tOS: {sys.system} {sys.release} \n") #
    textfile.write(f"\tMachine Name: {sys.node}\n")
    textfile.write(f"\tVersion: {sys.version}\n")
    textfile.write(f"\tCPU: {sys.processor}\n")
    textfile.write("\tNumber of Cores: " + str(psutil.cpu_count()) + "\n")
    textfile.write(f"\tRAM: {psutil.virtual_memory()}\n")
    textfile.write("---------------------------------------------------------------------------------\n")
    textfile.write("OUTPUT LOG:\n")

    for i in foundNumbers:
        textfile.write(str(i) + "\n")
    textfile.write("Elapsed Time:   " + str(timeStop-timeStart))

    textfile.close()

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


    modeSelect = None;
    print("Welcome to ParaBench! Please enter [1] to begin benchmarking, or [0] to exit." + '\n')
    modeSelect = int(input("[1] -> Begin Benchmarking \n[0] -> Exit\n" +
        "_________________________________________________________________________________\n"))


    #User selects Integer benchmarking mode
    if modeSelect == 1:
        print("Below are the available benchmarks for you to run. Searching for " +
            "mersenne numbers Mp that generate a prime number.")

        #Printout of selection for order of magnitude
        print("[1] -> First 1 x 10^2 Primes\n[2] -> First 1 x 10^3 Primes\n[3] ->" +
            " First 1 x 10^4 Primes \n[4] -> First 1 x 10^5 Primes\n[5] -> First 5 x 10^3 (BALANCED/STANDARD BENCHMARK)\n[0] -> Abort")
        mersenneOrder = int(input("Please Select an option\n" +
            "_________________________________________________________________________________\n"))
        foundNumbers = []
        percent = 0
        if mersenneOrder == 1:
            print("Starting Benchmark...")
            print("Mersenne numbers Mp for that form primes:")

            with ProcessPoolExecutor(15) as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,100)):
                    if result != None:
                        percent = (result / 100) * 100
                        print(str(result) + "        " + str(percent) + "% Done...\n")
                        foundNumbers.append(result)
                timeStop = perf_counter()

                #Display output to console once done
                print("1E2 Benchmark Complete in ",timeStop-timeStart)
                logging()


        if mersenneOrder == 2:
            print("Starting Benchmark...")
            with ProcessPoolExecutor(15) as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,1000)):
                    if result != None:
                        percent = (result / 1000) * 100
                        print(str(result) + "        " + str(percent) + "% Done...\n")                                         # TODO: Print % complete alongside results
                        foundNumbers.append(result)
                timeStop = perf_counter()

                print("1E3 Benchmark Complete!!", timeStop-timeStart)
                logging()

        if mersenneOrder == 3:
            print("Starting Benchmark...")
            with ProcessPoolExecutor() as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,10000)):
                    if result != None:
                        percent = (result / 10000) * 100
                        print(str(result) + "        " + str(percent) + "% Done...\n")
                        foundNumbers.append(result)
                timeStop = perf_counter()

                print("1E4 Benchmark Complete!!", timeStop-timeStart)
                logging()


        if mersenneOrder == 4:
            print("Starting Benchmark...")
            with ProcessPoolExecutor(15) as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,100000)):
                    if result != None:
                        percent = (result / 100000) * 100
                        print(str(result) + "        " + str(percent) + "% Done...\n")
                        foundNumbers.append(result)
                timeStop = perf_counter()

                print("1E5 Benchmark Complete!!", timeStop-timeStart)
                logging()

        #STANDARD BENCHMARK
        if mersenneOrder == 5:
            print("Starting Benchmark...")
            with ProcessPoolExecutor(15) as executor:
                timeStart = perf_counter()

                for result in executor.map(lehmer,range(2,5000)):
                    if result != None:
                        percent = (result / 5000) * 100
                        print(str(result) + "        " + str(percent) + "% Done...\n")
                        foundNumbers.append(result)
                timeStop = perf_counter()

                print("Benchmark Complete!!", timeStop-timeStart)
                logging()

        #Aborts if user decides to quit before benchmarking
        if mersenneOrder == 0:
            print("User Aborted.")

    #Ends program on user choice
    if modeSelect == 2:
        print("User chose to exit." )
