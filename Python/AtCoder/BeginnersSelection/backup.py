
w_lis = "dream dreamer erase eraser".split(" ")
l_lis = [len(w) for w in w_lis]

class Fail:
    def read(self, word):
        return self
    ok = False

class R:
    def __init__(self, s):
        self.s = s

    def read(self, word):
        ll = len(word)
        if self.s.startwith(word):
            return Token(self.s[ll:])
        else:
            return Fail()

    ok = True

def parse(s):
    token = Token(s)
    while True:
        dream = token.read("dream")
        if dream.read("erase").or_.read("er"):
            pass
        erase = token.read("erase")
        if erase.read("r"):
            pass
    found = False
    ans = 0
    for w, lngt in zip(w_lis, l_lis):
            ans = sea(new_x)
            if ans == True:
                found = True
                break
    return found
