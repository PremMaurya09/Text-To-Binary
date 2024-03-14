data = ['1100001','1100010','1100011','1100101','1100110','1100111','1101000','1101001','1101010','1101011','1101100','1101101','1101110','1101111','1110000', '1110001','1110010','1110011','1110100','1110101','1110110','1110111','1111000','1111001 ','1111010']

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_cap = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

data_cap = ['1000001','1000010','1000011','1000100','1000101','1000110','1000111','1001000','1001001','1001010','1001011','1001100','1001101','1001110','1001111','1010000','1010001','1010010','1010011','1010100','1010101','1010110','1010111','1011000','1011001','1011010']

input =input("Write something to convert it : ")
input_lst = []


for letter in input:
    input_lst.append(letter)

for i in range(0,len(input)):
    
        if input_lst[i] == alphabet[0]:
            input_lst[i] = data[0]
        elif input_lst[i] == alphabet[1]:
            input_lst[i] = data[1]
        elif input_lst[i] == alphabet[2]:
            input_lst[i] = data[2]
        elif input_lst[i] == alphabet[3]:
            input_lst[i] = data[3]
        elif input_lst[i] == alphabet[4]:
            input_lst[i] = data[4]
        elif input_lst[i] == alphabet[5]:
            input_lst[i] = data[5]
        elif input_lst[i] == alphabet[6]:
            input_lst[i] = data[6]
        elif input_lst[i] == alphabet[7]:
            input_lst[i] = data[7]
        elif input_lst[i] == alphabet[8]:
            input_lst[i] = data[8]
        elif input_lst[i] == alphabet[9]:
            input_lst[i] = data[9]
        elif input_lst[i] == alphabet[10]:
            input_lst[i] = data[10]
        elif input_lst[i] == alphabet[11]:
            input_lst[i] = data[11]
        elif input_lst[i] == alphabet[12]:
            input_lst[i] = data[12]
        elif input_lst[i] == alphabet[13]:
            input_lst[i] = data[13]
        elif input_lst[i] == alphabet[14]:
            input_lst[i] = data[14]
        elif input_lst[i] == alphabet[15]:
            input_lst[i] = data[15]
        elif input_lst[i] == alphabet[16]:
            input_lst[i] = data[16]
        elif input_lst[i] == alphabet[17]:
            input_lst[i] = data[17]
        elif input_lst[i] == alphabet[18]:
            input_lst[i] = data[18]
        elif input_lst[i] == alphabet[19]:
            input_lst[i] = data[19]
        elif input_lst[i] == alphabet[20]:
            input_lst[i] = data[20]
        elif input_lst[i] == alphabet[21]:
            input_lst[i] = data[21]
        elif input_lst[i] == alphabet[22]:
            input_lst[i] = data[22]
        elif input_lst[i] == alphabet[23]:
            input_lst[i] = data[23]
        elif input_lst[i] == alphabet[24]:
            input_lst[i] = data[24]
        elif input_lst[i] == alphabet[25]:
            input_lst[i] = data[25]

        
        
        elif input_lst[i] == alphabet_cap[0]:
            input_lst[i] = data_cap[0]
        elif input_lst[i] == alphabet_cap[1]:
            input_lst[i] = data_cap[1]
        elif input_lst[i] == alphabet_cap[2]:
            input_lst[i] = data_cap[2]
        elif input_lst[i] == alphabet_cap[3]:
            input_lst[i] = data_cap[3]
        elif input_lst[i] == alphabet_cap[4]:
            input_lst[i] = data_cap[4]
        elif input_lst[i] == alphabet_cap[5]:
            input_lst[i] = data_cap[5]
        elif input_lst[i] == alphabet_cap[6]:
            input_lst[i] = data_cap[6]
        elif input_lst[i] == alphabet_cap[7]:
            input_lst[i] = data_cap[7]
        elif input_lst[i] == alphabet_cap[8]:
            input_lst[i] = data_cap[8]
        elif input_lst[i] == alphabet_cap[9]:
            input_lst[i] = data_cap[9]
        elif input_lst[i] == alphabet_cap[10]:
            input_lst[i] = data_cap[10]
        elif input_lst[i] == alphabet_cap[11]:
            input_lst[i] = data_cap[11]
        elif input_lst[i] == alphabet_cap[12]:
            input_lst[i] = data_cap[12]
        elif input_lst[i] == alphabet_cap[13]:
            input_lst[i] = data_cap[13]
        elif input_lst[i] == alphabet_cap[14]:
            input_lst[i] = data_cap[14]
        elif input_lst[i] == alphabet_cap[15]:
            input_lst[i] = data_cap[15]
        elif input_lst[i] == alphabet_cap[16]:
            input_lst[i] = data_cap[16]
        elif input_lst[i] == alphabet_cap[17]:
            input_lst[i] = data_cap[17]
        elif input_lst[i] == alphabet_cap[18]:
            input_lst[i] = data_cap[18]
        elif input_lst[i] == alphabet_cap[19]:
            input_lst[i] = data_cap[19]
        elif input_lst[i] == alphabet_cap[20]:
            input_lst[i] = data_cap[20]
        elif input_lst[i] == alphabet_cap[21]:
            input_lst[i] = data_cap[21]
        elif input_lst[i] == alphabet_cap[22]:
            input_lst[i] = data_cap[22]
        elif input_lst[i] == alphabet_cap[23]:
            input_lst[i] = data_cap[23]
        elif input_lst[i] == alphabet_cap[24]:
            input_lst[i] = data_cap[24]
        elif input_lst[i] == alphabet_cap[25]:
            input_lst[i] = data_cap[25]

        else:
            input_lst[i] = input_lst[i]

final = ""

for i in input_lst:
    final += "0" +i + " "

print(final)