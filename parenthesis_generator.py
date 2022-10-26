def generateParenthesis(cap):
    egress_list = ["("*cap+")"*cap]
    digits_list = [[cap]]
    for j in digits_list:
        a = j[len(j)-1]
        for i in range(1, a):
            temp_list = j[:len(j)-1] + [i] + [a-i]
            digits_list.append(temp_list[:])
            egress_list.append("".join(["("*_ + ")"*_ for _ in temp_list]))
    return digits_list, egress_list


class Solution:
    total_list = []

    @staticmethod
    def generateParenthesis_bf(cap, current_loop, opened=0, closed=0, prthss="(", seq=""):
        if prthss == "(":
            next_prthss = ")"
        else:
            next_prthss = "("
        for i in range(1, current_loop + 1):
            if prthss == "(":
                opened += 1
                next_loop = opened - closed
            else:
                closed += 1
                next_loop = cap - opened
            seq += prthss
            if closed == cap:
                Solution.total_list.append(seq)
            Solution.generateParenthesis_bf(cap, next_loop, opened, closed, next_prthss, seq)

    def generateParenthesis(self, n: int):
        Solution.total_list.clear()
        Solution.generateParenthesis_bf(n, n)
        return Solution.total_list


s = Solution()
for _ in range(1, 5):
    s.generateParenthesis(_)
    [print(x) for x in Solution.total_list]
    print("Length: ", len(Solution.total_list))

# all_combos = generateParenthesis(cap)
# [print(x) for x in all_combos]
# print(len(all_combos))
