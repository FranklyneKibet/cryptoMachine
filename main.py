def cryptoMachine(): 
    
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]
    
    encryptDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))
    
    message = input('please enter your secret message : ')
    mode = input('Please select a mode: Encode(E) or Decode(D) : ')
    
    if mode.upper() == 'E':  
        newMessage = ''.join([encryptDict[letter] for letter in message.lower()])
    elif mode.upper() == 'D': 
        newMessage = ''.join([decryptDict[letter] for letter in message.lower()])
    else:  
        print('Please enter the correct choice')
        
    return newMessage

print(cryptoMachine())