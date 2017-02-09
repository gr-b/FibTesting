# Divide and Conquer vs. Brute force Algorithm test
# Author: Griffin Bishop

# Imports
import time
import math
######### Check if we can use matplotlib #######
plotlib_installed = True
try:
        import numpy as np
        import matplotlib.pyplot as plt
except:
        plotlib_installed = False
################################################


###### Functions ###############################

# Consumes an integer n for which it will
# produce the nth fibonnaci number recursively.
# Fibonnacii number are:
# n      0  1  2  3  4  5  6  7
# fib(n) 0  1  1  2  3  5  8  13
def fib_rec(n):
	if n is 0:
		return 0
        elif n is 1:
                return 1
	else:
		return fib_rec(n-1) + fib_rec(n-2)

# Consumes an integer n for which it will
# produce the nth fibonnaci number iterively
def fib_iter(n):
        if n is 0:
                return 0 # Edge case

        # Declare two variables to start 
        # The first two in the sequence: n = 0, n = 1
        a = 0
        b = 1
        while n>1:
                newb = a + b
                a = b
                b = newb
                n = n - 1
        return b
                

# Returns the time it takes to process the function given
def time_process(func):
	start = time.time()
	# Now perform the task
        func()
        elapsed_time = time.time()-start
	return elapsed_time

# Prints all nth fibonacci numbers up to the number given
def all_fib(func, n):
        for i in range(n):
                print(func(i))
        print(func(n))

# Samples the function given until the standard error is below
# the given number. 
# Starts with 10 samples.
def sample(func, error):
        samples = [func() for n in range(10)]
        st_dev = np.std(samples)
        avrg = np.average(samples)
        print(st_dev)
        plt.ion()
        plt.plot(samples[1:], c='blue') # discard the first result, it's always off
        plt.title("Std dev:" + str(st_dev) + "avg:" + str(avrg))
        plt.xlabel("Number of samples")
        plt.ylabel("Time to calculate")
        plt.show()

def sample2(func, error):
        samples = [func()]
        sigmas = []
        averages = []
        std_err = []
        indices = [1]
        plt.ion()
        #plt.plot(samples, c='blue')
        plt.show()
        
        for x in range(100):
                samples = samples + [func()]
                indices = indices + [indices[-1] + 1] # add one to last in indices
                #plt.plot(samples, c='blue')
                
                averages = averages + [np.average(samples)]
                sigmas = sigmas + [np.std(samples)]
                std_err = std_err + [sigmas[-1]/math.sqrt(len(indices))]

                plt.plot(averages, c='red')
                #plt.plot(sigmas, c='purple')
                #if len(sigmas)>5:
                 #       plt.plot(np.gradient(sigmas), c='green')
                plt.plot(std_err, c='yellow')
                plt.draw()
                time.sleep(0.05)
        time.sleep(5)

# Perform the given function the given number n amount
# of times and then return the average produced.
def sample_average(func, n):
        samples = []
        for x in range(n):
                samples = samples + [func()]
                #if reduce(lambda x,y: x+y, samples)/len(samples) > 0.15:
                 #       return 11
        average = reduce(lambda x,y: x+y, samples)/len(samples)
        return average
        
# Creates a cumulative plot of the times of the
# fibonnacci sequence 
def cum_plot(func, n, color, accuracy, title):
	# Populate values 
	times = []
	indices = []

        if use_graphs:
                plt.ion()
                plt.plot(indices, times, c='blue')
                plt.show()	
        
        start = time.time() # Start 2 minute timer

	for x in range(n):
		atime = sample_average(lambda: time_process(
                        lambda: func(x)), accuracy)
		times = times + [atime]
                indices = indices + [x]
                #If the current time running is more than 2 mins, 
                #break out of loop
                time_running = int(time.time()-start)

                if use_graphs:
                        plt.title(title + " Times run: " + 
                                  str(x) + " Running time: " 
                                  + str(time_running))
                        plt.xlabel("n")
                        plt.ylabel("fib(n)")
                        plt.plot(indices, times, c=color)
                        plt.draw()
                else:
                        fileone.write(title + "- n: " + str(x) 
                                      + " Time: " + str(atime) + "\n")

		time.sleep(0.05)
        if use_graphs:
                plt.savefig("plot.png")
        return times

def avg_array(arrays):
        retArray = []
        for x in range(len(arrays[0])):
                curr_avg = 0
                for y in range(len(arrays)):
                        #add all the first elements
                        curr_avg = curr_avg + arrays[y][x]
                curr_avg = curr_avg / len(arrays)
                retArray = retArray + [curr_avg]
        return retArray

def cum_plot2(func, n, color, accuracy):
        times = [time_process(lambda: func(x)) for x in range(n)]
        plt.ion()
        plt.plot(times, c=color)
        plt.show()
        
        timeArrays = []

        for i in range(accuracy):
                tempTimes = []
                for x in range(n):
                        atime = time_process(lambda: func(x))
                        tempTimes = tempTimes + [atime]
                timeArrays = timeArrays + [tempTimes]        
                #times = [(times[i]+tempTimes[i])/2 for i in range(len(times))]
                times = avg_array(timeArrays)
                plt.clf()
                plt.title("Run: " + str(i))
                plt.plot(times, c=color)
                plt.draw()
                time.sleep(0.05)

# Asks the user the enter 1 or 0,
# prompting them with the given message.
# If they don't enter either,
# ask them until they do. 
def enter_0_or_1(msg):
        entered_num = -1

        while entered_num is not 1 and entered_num is not 0:
                try:
                        entered_num = int(raw_input(msg))
                except:
                        print("You did not enter either 0 or 1. Try again.")
        return entered_num

###### End functions ######


######     Menu      ######
print("======Fibonacci - Recursive vs. Iterative======")
print("============Author: Griffin Bishop=============")
if not plotlib_installed:
        print("NOTE: matplotlib is not installed. Trying to use graphs will")
        print("result in errors.")
use_graphs = enter_0_or_1("Do you want to show graphs? (0 for no, 1 for yes) ")

print("Do you want to test the divide and conquer (0) ")
use_brute_force = enter_0_or_1("or the brute force algorithm (1)? ")

print("Do you want to calculate all up to a number entered (0) ")
calc_one_number = enter_0_or_1("or just one number many times (1)? ")

print("=============================================")
if calc_one_number:
        print("You selected calculating one number many times.")
        num = int(raw_input("Enter a number to calculate: "))
else:
        print("You selected calculating all up to one number")
        num = int(raw_input("Enter a number to calculate: "))

accuracy = int(raw_input("Enter the number of times to calculate the number or"
                + " each number (higher is more accurate, but slower):"))

if use_brute_force:
        algorithm = fib_iter
        title = "Brute Force"
        color = "blue"
else: # If not use_brute_force
        algorithm = fib_rec
        title = "Divide and Conquer"
        color = "red"


if calc_one_number:
        #sample_mean(fib_iter, num, 'blue', accuracy, "Brute Force")
        func = lambda x: algorithm(num)
        num = accuracy
        accuracy = 1
elif not calc_one_number:
        #func(fib_rec, num, 'red', accuracy, "Divide and Conquer")
        func = lambda x: algorithm(x)
else:
        print("Something went wrong.") # Should never get here.

fileone = open("log.txt","w")
# Finally, put it all together into the function call
times = cum_plot(func, num, color, accuracy, title)

if use_graphs:
        plt.close()
        plt.plot(times, c=color)
        plt.title(title)
        plt.show(block=True)


