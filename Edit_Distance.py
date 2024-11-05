"""
Edit Distance Calculator
This program calculates the Levenshtein distance between two words and displays
the calculation matrix and optimal alignment.

To run this program:
1. Ensure Python 3.x is installed on your system
2. Save this file as Edit_Distance.py
3. Run: python3 Edit_Distance.py on your terminal
4. Enter two words when prompted
5. The program will display the edit distance, matrix, and optimal alignment

Note: For reference the top of the matrix is the second word and the left side is the first word.
"""

def create_matrix(word1, word2):
    rows = len(word1) + 1
    cols = len(word2) + 1
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Initialize first row and column
    for i in range(rows):
        matrix[i][0] = i
    for j in range(cols):
        matrix[0][j] = j
        
    # Fill in the rest of the matrix
    for i in range(1, rows):
        for j in range(1, cols):
            if word1[i-1] == word2[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(
                    matrix[i-1][j] + 1,    # deletion
                    matrix[i][j-1] + 1,    # insertion
                    matrix[i-1][j-1] + 1   # substitution
                )
    
    return matrix

def print_matrix(matrix, word1, word2):
    # Print header row with second word
    print("The matrix:")
    print(" " * 4, end="")
    print(" " * 3, end="")
    for j in range(len(word2) + 1):
        print(f"{j:2d}", end=" : ")
    print()
    
    # Print each row
    for i in range(len(matrix)):
        print(f"{i:2d} |", end=" ")
        for j in range(len(matrix[0])):
            print(f"{matrix[i][j]:2d}", end=" : ")
        print()

def find_alignment(matrix, word1, word2):
    # Backtrack through the matrix to find the optimal alignment
    i = len(word1)
    j = len(word2)
    alignment1 = []
    alignment2 = []
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and word1[i-1] == word2[j-1]:
            alignment1.append(word1[i-1])
            alignment2.append(word2[j-1])
            i -= 1
            j -= 1
        elif i > 0 and (j == 0 or matrix[i][j] == matrix[i-1][j] + 1):
            alignment1.append(word1[i-1])
            alignment2.append("_")
            i -= 1
        else:
            alignment1.append("_")
            alignment2.append(word2[j-1])
            j -= 1
    
    # Reverse the alignments since we built them backwards
    return ''.join(reversed(alignment1)), ''.join(reversed(alignment2))

def main():
    print("Welcome to Edit Distance Demonstration.*")
    print("\nPlease input two words for the edit distance:")
    
    word1 = input("The first word: ")
    word2 = input("The second word: ")
    
    # Calculate edit distance matrix
    matrix = create_matrix(word1, word2)
    
    # Print the matrix
    print_matrix(matrix, word1, word2)
    
    # Print the edit distance
    edit_distance = matrix[-1][-1]
    print(f"\nThe edit distance is: {edit_distance}")
    
    # Find and print the alignment
    alignment1, alignment2 = find_alignment(matrix, word1, word2)
    print("\nAlignment is:")
    print(alignment1)
    print(alignment2)

if __name__ == "__main__":
    main()