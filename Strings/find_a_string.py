def count_substring(string, sub_string):
    string_list = list()
    length = len(sub_string)
    for i in range(len(string)-length+1):
        string_list.append(string[i:i+length])
    return string_list.count(sub_string)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
