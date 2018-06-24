#Cameron Chromiak
#June 24 2018
# algorithm to take a string of any length get first letter of each word, and
#disregard everything else ie [] . , ! ?


def getFirstLetter(userString):
    #userString = "The sentence has spaces and symbols [4x] !"
    unWantedChar = "!,[]?."
    for char in unWantedChar: #removes symbols
        userString = userString.replace(char, "")
    print(userString)
    output = ""
    for i in userString.upper().split():
        output += i[0]
    print(output)
                

def main():
    userString = input("Enter a string: ")
    getFirstLetter(userString)
    
main()


##    for char in userString:
##        if char[0] == "4" and char[1] == "x":
##            userString = userString.replace(char, "")
    
#need way to remove numbers only if preceding an 'x' to indicate repeat of lyrics
#fix one big string eg: one.big.dog! will produce abigdog
