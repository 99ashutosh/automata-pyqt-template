class plemma:
    def getString(s):
        global d
        d=""
        for i in range(s//2):
            d += "".join("a")
        for i in range(s//2):
            d += "".join("b")
        return d

    def splitStrings(x,y,z):
        x_str = d[0:x]
        y_str = d[x:y]
        if (z!=0):
            z_str = d[y:len(d)-1]
            return x_str,y_str,z_str
        return x_str,y_str

