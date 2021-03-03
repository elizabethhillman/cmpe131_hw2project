"imports time"
import time

'''this decorator will calculate the time to run a function
Parameter:
func: the function being wrapped
Return:
the time in seconds for a function to run, the wrapper'''


def calculate_time(func):
    def wrapper():
        "stores time before function called"
        start_time = time.time()
        "calls function"
        func()
        "stores time after function"
        time_after_function = time.time()
        "calculate total time"
        x = time_after_function - start_time
        print("Total time " + str(x))
    "returns the wrapper"
    return wrapper

"used for testing"
@calculate_time
def tester():
    time.sleep(2)


tester()

