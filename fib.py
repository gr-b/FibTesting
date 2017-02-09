# Divide and Conquer vs. Brute force Algorithm test
# CS2223 - Mello-Stark
# Author: Griffin Bishop
######
# This implementation calculates the fibonacci sequence in a few different
# ways, and records the time it takes to calculate them. It can do it 
# using a brute force method or a divide and conquer method. It can also 
# calculate one number of the sequence many times, to see variation. 
# It can also calculate each number several times in and take the average
# time in order to get more accurate results.
#####

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

# Perform the given function the given number n amount
# of times and then return the average produced.
def sample_average(func, n):
        samples = []
        for x in range(n):
                samples = samples + [func()]
        average = reduce(lambda x,y: x+y, samples)/len(samples)
        return average
        
# Creates a plot of the times of the
# fibonnacci sequence with the algorithm given. 
# Graphs the data if that option is enabled.
def fib_plot(func, n, color, accuracy, title):
	# declare values 
	times = []
	indices = []

        if use_graphs:
                plt.ion()
                plt.plot(indices, times, c='blue')
                plt.show()	
        
        start = time.time() # Start 2 minute timer

	for x in range(n):
                # Calculate the next time.
		atime = sample_average(lambda: time_process(
                        lambda: func(x)), accuracy)
		times = times + [atime]
                indices = indices + [x]

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
                        print(title + "- n: " + str(x) 
                              + " Time: " + str(atime))
		time.sleep(0.05)

        if use_graphs:
                plt.savefig("plot.png")

        return times

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

print("To quit during execution, press Control-Z on linux.")

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

# Finally, put it all together into the function call
times = fib_plot(func, num, color, accuracy, title)





if use_graphs:
        indices = [x for x in range(len(times))]
        par = np.polyfit(indices,times, 1, full=True)

        par2 = np.polyfit(indices,times, 2, full=True)


# End with showing them the final graph, if enabled.
if use_graphs:
        plt.close()
        plt.plot(times, c=color)
        plt.plot(indices, np.poly1d(np.polyfit(indices, times, 1))(indices))
        plt.title(title)
        plt.show(block=True)



