import sys
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()

def calculate_minimum_students():
    p_coincident_birthday = float(input("Enter probability that at least two students have the same birthday (in decimal) : "))
    while not (p_coincident_birthday >= 0 and p_coincident_birthday <= 1):
        print("The value must be in the range [0,1] !")
        p_coincident_birthday = float(input("Enter probability that at least two students have the same birthday (in decimal) : "))
    
    # Converts p into a decimal value

    # Finding the required probability of no two students having the same birthday
    p_n = 1 - p_coincident_birthday

    # p_k is the probability of no two students having the same birthday when there are k students in the class
    # for limiting case, there is only one student (k = 1) in the class and thereby the probability of no two students having the same birthday is 1
    p_k = 1.0
    k = 1

    # Loop along the probability of this not happening
    while ((p_k > p_n) and p_n != 0):
        # if p_k is still not small enough, we increase the class strength by one
        p_k = p_k * (365 - k) / 365
        k += 1

    # for the case when 100% probability is required we can use PHP to say that it will be true for k=366. For k=365 it is still possible that every person has a different birthday
    if p_n == 0:
        k = 366

    print("The minimum number of students required will be : ", k)

def graph():
    # Plotting graph
    n = 100

    distribution = []
    prob_no_match = 1
    for i in range(n):
        prob_no_match = prob_no_match * ((365 - i)/365)
        distribution.append(1 - prob_no_match)

    plt.title("Birthday Paradox")
    plt.xlabel("Number of People")
    plt.ylabel("Probabilty of a Matching Birthday")
    plt.axis([0,n,0,1])

    plt.plot(range(1,n+1), distribution)
    plt.show()

# Main program
def main():
    if len(sys.argv) < 2:
        calculate_minimum_students()

    elif sys.argv[1] == "graph":
        graph()
    else:
        print("Invalid operation. Please provide a valid operation.")

if __name__ == "__main__":
    main()