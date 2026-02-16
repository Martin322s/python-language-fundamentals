string = input()

result_dict = { 'digits': [], 'letters': [], 'other': [] }

for i in range(len(string)):
    if string[i].isdigit():
        result_dict['digits'].append(string[i])
    elif string[i].isalpha():
        result_dict['letters'].append(string[i])
    else:
        result_dict['other'].append(string[i])
        
print("".join(result_dict.get('digits')))
print("".join(result_dict.get('letters')))
print("".join(result_dict.get('other')))