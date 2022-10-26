height = list(input("Enter an array split by a space: ").split())

class TrapArray():
    def trap(self, height):
        lst_tmp = []
        vol0 = 0
        for i, c0 in enumerate(height):
            c0 = int(c0)
            if i==0:continue
            c1 = int(height[i - 1])
            bottom0 = c1
            if c1 > c0:
                lst_tmp.append([c1, i])
                continue
            if c1 < c0 and len(lst_tmp)>0:
                while len(lst_tmp) > 0 :
                    bottom1 = min(c0, lst_tmp[-1][0])
                    vol1 = (i - lst_tmp[-1][1]) * (bottom1 - bottom0)
                    vol0 += vol1
                    bottom0 = bottom1
                    if c0 < lst_tmp[-1][0]: break
                    if c0 >= lst_tmp[-1][0]:
                        last = lst_tmp.pop()
                        if c0 == last[0] :
                            break
        return vol0

obj = TrapArray()
print("Volume of flood: %d" % obj.trap(height))
