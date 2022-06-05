#Importing modules
import sys
import time
import psutil

"""
Defining the global variables (The hardcoded values as per the project document)
DELTA: The gap penalty.
ALPHAS_DICT: A dictionary that stores a pair of alphabets as key and their mismatch cost as values.
"""
DELTA = 30
ALPHAS_DICT = {}
ALPHAS_DICT[("A","A")] = 0
ALPHAS_DICT[("A","C")] = 110
ALPHAS_DICT[("A","G")] = 48
ALPHAS_DICT[("A","T")] = 94

ALPHAS_DICT[("C","A")] = 110
ALPHAS_DICT[("C","C")] = 0
ALPHAS_DICT[("C","G")] = 118
ALPHAS_DICT[("C","T")] = 48

ALPHAS_DICT[("G","A")] = 48
ALPHAS_DICT[("G","C")] = 118
ALPHAS_DICT[("G","G")] = 0
ALPHAS_DICT[("G","T")] = 110

ALPHAS_DICT[("T","A")] = 94
ALPHAS_DICT[("T","C")] = 48
ALPHAS_DICT[("T","G")] = 110
ALPHAS_DICT[("T","T")] = 0

"""
readInputFile function takes file Path (of input file) as input.
It reads the file to get the two base input strings and the respective integers to generate the final two input strings.

Input parameters:-
inputFilePath: path to the input file.

Output:-
firstInput: first base string.
secondInput: second base string.
firstStringGenerationList: list of int values needed to generate the first input string from the first base string.
secondStringGenerationList: list of int values needed to generate the second input string from the second base string.
"""
def readInputFile(inputFilePath):
    inputFile = open(inputFilePath,"r")
    inputLines = inputFile.readlines()
    inputFile.close()
    
    firstInput =""  #First base string
    secondInput = "" #Second base string 
    firstStringGenerationList = [] #A list of integer values required to generate the first final string
    secondStringGenerationList = [] #A list of integer values required to generate the second base string
    
    isFirstInputRead = False
    isFirstInputProcessed = False
    
    for i in inputLines:
        if isFirstInputRead == False and i.strip().isalpha() == True:
            firstInput = i.strip()
            isFirstInputRead = True
            
        elif isFirstInputRead == True and i.strip().isalpha() == True:
            secondInput = i.strip()
            isFirstInputProcessed = True
            
        elif isFirstInputProcessed == False and i.strip().isnumeric() == True:
            firstStringGenerationList.append(int(i.strip()))
            
        elif isFirstInputProcessed == True and i.strip().isnumeric() == True:
            secondStringGenerationList.append(int(i.strip()))

    return firstInput, secondInput, firstStringGenerationList, secondStringGenerationList
            

"""
generateInputString generates the two final input strings from the base strings

Input parameters:-
s1: first base string
jList: The list of int values needed to generate first final string from the first base string
s2: second base string
kList: The list of int values needed to generate second final string from the second base string

Output:
firstInputString: The first input string generated from the first base string.
secondInputString: The second input string generated from the second base string.
"""

def generateInputString(s1,jList,s2,kList):
    firstInputString = s1 #first base string
    secondInputString = s2 #second base string 
    for j in jList:
        firstInputString = firstInputString[:j+1] + firstInputString + firstInputString[j+1:]
    
    for k in kList:
        secondInputString = secondInputString[:k+1] + secondInputString + secondInputString[k+1:]
    
    return firstInputString,secondInputString

"""
basicDPSolver finds the optimal string alignment between two strings using dynamic programming.

Input parameter:-
firstString: The first input string
secondString: The second input string

Output: alignment cost for the two stringis, First aligned string, second aligned string
"""
def basicDPSolver(firstString,secondString):
    
    m = len(firstString) #Length of the first input string
    n = len(secondString) #Length of the second input string
    
    #initializing the 2-D DP matrix which strores the optimal intermediate string alignmet costs
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for j in range(n+1):
        dp[0][j] = DELTA*j
        
    for i in range(m+1):
        dp[i][0] = DELTA*i

    #populating the DP matrix based on the recurrence relation 
    for i in range(1,m +1):
        for j in range(1,n+1):
            dp[i][j] = min(ALPHAS_DICT[(firstString[i-1],secondString[j-1])] + dp[i-1][j-1], DELTA+dp[i-1][j], DELTA+dp[i][j-1]) #The recurrence relation
    
    #constructing the two aligned strings
    firstFinalStringReversed = ""
    secondFinalStringReversed = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if dp[i][j] == (ALPHAS_DICT[(firstString[i-1],secondString[j-1])] + dp[i-1][j-1]) :
            firstFinalStringReversed += firstString[i-1]
            secondFinalStringReversed += secondString[j-1]
            i-=1
            j-=1

        elif dp[i][j] == DELTA+dp[i][j-1] :
            firstFinalStringReversed += '_'
            secondFinalStringReversed += secondString[j-1]
            j-=1

        elif dp[i][j] == DELTA+dp[i-1][j]:
            firstFinalStringReversed += firstString[i-1]
            secondFinalStringReversed += '_'
            i-=1

    while i > 0:
        firstFinalStringReversed += firstString[i-1]
        secondFinalStringReversed += '_'
        i-=1 

    while j > 0:
        firstFinalStringReversed += '_'
        secondFinalStringReversed += secondString[j-1]
        j-=1
        
    return dp[m][n],firstFinalStringReversed[::-1],secondFinalStringReversed[::-1]

"""
memorySavingSolution function solves the string alignment problem using the basic dynamic programming but it uses only two required rows.

Input parameters:-
firstString: The first input string
secondString: The second input string

Output:-
string alignment cost
"""
def memorySavingSolution(firstString,secondString):
    m = len(firstString) #length of first input string
    n = len(secondString) #length of second input string 
    dp = [[0 for i in range(n+1)] for j in range(2)]

    for j in range(n+1):
        dp[0][j] = DELTA*j        

    for i in range(1,m+1):
        dp[1][0] = i*DELTA
        
        for j in range(1,n+1):
            dp[1][j] = min(ALPHAS_DICT[(firstString[i-1],secondString[j-1])] + dp[0][j-1], DELTA+dp[0][j], DELTA+dp[1][j-1])
            
        for k in range(n+1):
            dp[0][k] = dp[1][k]

    return dp[1]

"""
memoryEfficientSolver is a recursive function which uses basic dynamic programming and divide and conquer to solve the string alignment problem.

Input parameter:-
x: first input string 
y: second input string

Output:-
alignment cost, first aligned string, second aligned string 
"""
def memoryEfficientSolver(x,y):
    m = len(x) #length of the first input string
    n = len(y) #length of the second input string 

    if m <= 2 or n <= 2: #base case
        return basicDPSolver(x,y)
    
    splitPointX = m//2 #split point for first string x
    xL = x[:splitPointX] #first half of the first string x
    xR = x[splitPointX:] #second half of the first string x
    
    # finding the optimal split point for the second string y
    tempList1 = memorySavingSolution(xL,y)
    tempList2 = memorySavingSolution(xR[::-1],y[::-1])[::-1]
    sumList = [i+j for i,j in zip(tempList1,tempList2)]
    minIndex = sumList.index(min(sumList)) #split point for the second string y
    yL = y[:minIndex] #first half of the second string y
    yR = y[minIndex:] #second half of the second string y
    
    # Solving the problem recursively
    temp1_cost,temp1_string1,temp1_string2 = memoryEfficientSolver(xL,yL)
    temp2_cost,temp2_string1,temp2_string2 = memoryEfficientSolver(xR,yR)
    
    return temp1_cost + temp2_cost,temp1_string1+temp2_string1, temp1_string2+temp2_string2

"""
process_memory returns the memory consumed in KB.
This function has been taken from the project document.
"""
def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

"""
time_wrapper takes the function to be called and the arguments to be passed to the function. 
It calculates the time elapsed (in milli-seconds) in between the function (passed as argument) call.
Major part of this function has been taken from the project document,

Input parameters:-
func: The function to be called. In this case, its the memoryEfficientSolver function.  
*args: The arguments for the 'func' function. 

Output:-
All the outputs by the 'func' function (In this case it's the output by the memoryEfficientSolver function) along 
with the time elapsed in milli-seconds between the function call.
"""
def time_wrapper(func, *args):
    start_time = time.time()
    alignmentCost,firstStringAlignment,secondStringAlignment = func(*args)
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    return alignmentCost,firstStringAlignment,secondStringAlignment,time_taken



if __name__ == "__main__":

    # Reading the command line arguments
    inputFilePath = sys.argv[1]
    outputFilePath = sys.argv[2]
    
    # Reading the input file
    firstInput, secondInput, firstStringGenerationList, secondStringGenerationList = readInputFile(inputFilePath)

    # Generating the input strings
    firstInputString, secondInputString = generateInputString(firstInput,firstStringGenerationList,secondInput,secondStringGenerationList)

    # Solving the string alignment problem using basic dymainic programming + Divide and Conquer and getting the alignment cost, and two aligned strings along with the time elapsed in milli-seconds.
    alignmentCost,firstStringAlignment,secondStringAlignment, timeTaken = time_wrapper(memoryEfficientSolver,firstInputString,secondInputString)

    # Getting the memory consumed in KB
    memoryConsumed = process_memory()
    
    #  Writing the output to the output file.
    outputFile = open(outputFilePath, "w")
    outputFile.write(str(alignmentCost))
    outputFile.write("\n")
    outputFile.write(firstStringAlignment)
    outputFile.write("\n")
    outputFile.write(secondStringAlignment)
    outputFile.write("\n")
    outputFile.write(str(timeTaken))
    outputFile.write("\n")
    outputFile.write(str(memoryConsumed))
    outputFile.close()
