def knapSack(W, wt, val): 
    n=len(val)
    table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    #W is for columns, n for rows
    # i and j correspond to maximum profit

    for i in range(n + 1): 
        for j in range(W + 1): 
            
            if i == 0 or j == 0: 
                table[i][j] = 0
            
            elif wt[i-1] <= j: 
                table[i][j] = max(val[i-1] + table[i-1][j-wt[i-1]],  table[i-1][j]) 
            
            else: 
                table[i][j] = table[i-1][j] 
   
    return table[n][W] 


# --- taking the capacity of an array (value table) and build : ---
print("~~~WELCOME TO THE KNAPSACK SOLVER APP~~~")
# constructing value table :
val = []
capacity1 = int(input("\n\nHow many values you have? : "))
for x in range(capacity1):
    number1 = input("Enter a number to add : ")
    val.append(int(number1))
    if x == capacity1:
        break

print("\nYour value array is : ", val)

# constructing the weights table :
wt = []
capacity2 = int(input("\n\nHow many weights you have? : "))
for y in range(capacity2):
    number2 = input("Enter a number to add : ")
    wt.append(int(number2))
    if y == capacity2:
        break

print("\nYour weight array is : ", wt)

#WaitTime information :
W = int(input("\nWhat is your Wait Time value? : "))

print("\n\nYour Knapsack Dynamic Solution is : " , knapSack(W, wt, val))
