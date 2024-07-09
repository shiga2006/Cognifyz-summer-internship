#Level 2
#Task 5:File Manipulation
fname = input("Enter the file location and extension: ")
word = input("Enter the word to be searched: ")
k = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i == word):
                k = k + 1
print("Occurance of the word in the file is: ",k)
