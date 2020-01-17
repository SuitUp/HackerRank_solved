def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    for i in range(0, n, k):
        s = ""
        substr = string[i: i+k]
        for ele in substr:
            if ele not in s:
                s += ele
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    