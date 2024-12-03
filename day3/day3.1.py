with open('day3\input.txt', 'r') as file:
    # Read the entire contents of the file into a character buffer
    char_buffer = file.read()

Total = 0

for i in range(len(char_buffer)):
    if char_buffer[i] == 'm':
        if char_buffer[i+1] == 'u' :
             if char_buffer[i+2] == 'l':
                 if char_buffer[i+3] == '(' :
                    #Check that next 1, 2 or 3 characters are digits

                    ###,###)
                    seven_chars = char_buffer[i + 4:i + 12]
                    seven_chars = list(seven_chars)
                    print(f"Copied 7 characters: {seven_chars}")

                    charCnt =0 
                    addTo1 = True
                    addTo2 = False
                    oneFound = False
                    twoFound = False
                    isCompleted = False
                    firstNum = ""
                    secondNum = ""
                    i += 4

                    while len(seven_chars) > 0:
                        charCnt += 1
                        if seven_chars[0].isdigit() and addTo1:
                            oneFound = True
                            firstNum += seven_chars[0]
                            seven_chars.pop(0)
                        elif seven_chars[0] == ',':
                            addTo1 = False
                            addTo2 = True
                            seven_chars.pop(0)
                        elif seven_chars[0].isdigit() and addTo2:
                            twoFound = True
                            secondNum += seven_chars[0]
                            seven_chars.pop(0)
                        elif seven_chars[0] == ')':
                            if oneFound and twoFound:
                                isCompleted = True
                            seven_chars.pop(0)
                            break
                        else:
                             seven_chars.pop(0)
                    
                    print(f"Copied 7 characters: {firstNum}, {secondNum}. {isCompleted}")

                    if isCompleted:
                        Total += int(firstNum) * int(secondNum)
                        print(f"Total: {Total}")
                           

     




            


