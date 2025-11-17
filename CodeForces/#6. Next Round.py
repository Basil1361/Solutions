'''
memory limit per test
256 megabytes

"Contestant who earns a score equal to or greater than the k-th place finisher's score will advance to the next round, as long as the contestant earns a positive score..." — an excerpt from contest rules.

A total of n participants took part in the contest (n ≥ k), and you already know their scores. Calculate how many participants will advance to the next round.
Input

The first line of the input contains two integers n and k (1 ≤ k ≤ n ≤ 50) separated by a single space.

The second line contains n space-separated integers a1, a2, ..., an (0 ≤ ai ≤ 100), where ai is the score earned by the participant who got the i-th place. The given sequence is non-increasing (that is, for all i from 1 to n - 1 the following condition is fulfilled: ai ≥ ai + 1).
Output

Output the number of participants who advance to the next round.

'''

# n = number of participants
# k = scoring points

# condition
# k >= 1
# n >= k
# n <= 50

while True:
    try:
        n, k = map(int, input("Enter the values of n and k: ").split())
        if k >= 1 and n >= k and n <= 50:
            break
        else:
            print("Try again, retype")
    except ValueError:
        print("Try again, retype")
    
while True:
    try:
        scores = list(map(int, input(f"Enter {n} scores: ").split()))
        if len(scores) != n:
            print(f"Please enter exactly {n} values")
            continue
        if all(0 <= score <= 100 for score in scores):
            break
        else:
            print("All scores must be between 0 and 100")
    except ValueError:
        print("Try again, retype")
        
# Logic
count = 0
for i in range(n):
    if scores[i] > k:
        count += 1
print(count)


    

        
        
        
    