# import pywhatkit
# # syntax: phone number with country code, message, hour and minutes
# pywhatkit.sendwhatmsg('+919082054068', 'Hello I Am Ankit', 12, 52)




# 1 to 100 prime number:

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
n = 20

for i in range(2,20):
    for j in range(2,i//2+1):
        if i% j == 0:
        # if j % i == 0:
            break
        else:
            continue
    else:
        print(i)
        
