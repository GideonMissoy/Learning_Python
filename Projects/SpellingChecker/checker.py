from textblob import TextBlob

t = 1
while t:
    alpha = input("Enter the word to be checked:- ")
    print("original text: "+str(alpha))
    
    beta = TextBlob(alpha)
    
    # Prints the corrected spelling
    print("corrected text: "+str(beta.correct()))
    t = int(input("Try again? 1 : 0"))