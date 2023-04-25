def isBalanced(s):
    # while True:
    #     if "{}" in s:
    #         s=s.replace("{}", "")
    #     elif "()" in s:
    #         s=s.replace("()", "")
    #     elif "[]" in s:
    #         s=s.replace("[]","")
    #     else:
    #         break
    # if len(s)==0:
    #     return 'YES'
    # else:
    #     return 'NO'

    #dict = {"{": "}", "[": "]", "(": ")"}
    tab = []
    n = len(s)
    # for char in s:
    #     tab.append(char)
    for i in range(n//2):
        if s[i]==s[n-i-1]:
            s[i]=""
            s[n-i-1]=""
            continue
        else:
            break
    if len(tab)==0:
        return 'YES'
    else:
        return 'NO'





s="strrts"
print(isBalanced(s))


