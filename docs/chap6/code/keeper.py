#coding:utf-8

'''
    filename:keeper.py
    keep speical characters in a string.
'''



class Keeper:
    def __init__(self,keep):
        self.keep = set(map(ord,keep))

    def __getitem__(self,n):
        if n not in self.keep:
            return None
        return chr(n)
    def __call__(self,s):
        return s.translate(self)





vowels = Keeper('aeiouy')
print(vowels.keep)
for k in vowels.keep:
    print(k,vowels[k])

print(vowels('you raise me up.'))





