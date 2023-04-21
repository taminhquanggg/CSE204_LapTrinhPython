'''s = input('Nhập địa chỉ Email: ').split()
domain = ['@gmail.com', '@yahoo.com', '@vtv.vn']
def checkEmail(s):
    if s.count('@')==0 or s.count('.')==0:
        return False
    k = s.rfind('@')
    list1, list2 = s[:k], s[k:]
    for i in list1:
        if i.isdigit() or i.isalpha() or i.isnumeric():
            continue
        else: return False
    if list2[1:2]=='.' or list2[len(list2)-1:]=='.': return False
    return True
print(checkEmail(s))'''

def check(email):
    k = email.count('@')
    if k == 1:
        p = email.index('@')
        if p>0:
            if email.endswith('@gmail.com'):
                return True
    return False
email = input('Email của bạn: ')
print('Địa chỉ đúng!' if check(email) else 'Địa chỉ sai!')