from math import sqrt, floor
import re
from utils import verify_func


examples_path = "aab_examples.txt"


class AAB_issue():
    def __init__(self):
        super().__init__()

    #stack_list = {}
    div_dict = {}
    #div_qty_dict = {}
    current_stack = {}

    def find_aab_factors(self, n):
        if not n in self.current_stack:
            self.current_stack[n] = []
        # if not n in self.stack_list:
        #     self.stack_list[n] = []
        if not n in self.div_dict:
            self.div_dict[n] = []
        fl = False
        if n <= 5:
            self.div_dict[n] = [n]
            return self.div_dict[n]
        mult = 1
        sq_n = int(sqrt(n))
        for i0 in range(2, sq_n + 1):
            if n % i0 == 0:
                fl = True
                mult *= i0
                div = int(n / i0) - 1
                if div in self.div_dict:
                    self.current_stack[n].append(i0)
                    self.current_stack[n] += self.div_dict[div]
                    #self.stack_list[n].append(self.current_stack[n][:])
                    if len(self.div_dict[n]) < len(self.current_stack[n]):
                        self.div_dict[n] = self.current_stack[n][:]
                else:
                    self.current_stack[n].append(i0)
                    if div >= 6:
                        self.find_aab_factors(div)
                        self.current_stack[n] += self.div_dict[div]
                        #self.stack_list[n].append(self.current_stack[n][:])
                        if len(self.div_dict[n]) < len(self.current_stack[n]):
                            self.div_dict[n] = self.current_stack[n][:]
                    else:
                        self.current_stack[n].append(div)
                        if len(self.div_dict[n]) < len(self.current_stack[n]):
                            self.div_dict[n] = self.current_stack[n][:]
                        #self.stack_list[n].append(self.current_stack[n][:])
                        self.current_stack[n].pop()
                self.current_stack[n].clear()
        if not fl:
            self.div_dict[n] = [n]
            #self.current_stack[n].append(n)
            #if not n in self.stack_list:
            #    self.stack_list[n] = []
            #self.stack_list[n].append(self.current_stack[n][:])
            #self.current_stack[n].pop()
        else:
            div_n = int(n / mult)
            if div_n > sq_n:
                if mult - 1 >= 6:
                    self.current_stack[n].append(div_n)
                    if mult - 1 in self.div_dict:
                        self.current_stack[n] += self.div_dict[mult - 1]
                    else:
                        self.find_aab_factors(mult - 1)
                        self.current_stack[n] += self.div_dict[mult - 1]
                    #self.stack_list[n].append(self.current_stack[n][:])
                    if len(self.div_dict[n]) < len(self.current_stack[n]):
                        self.div_dict[n] = self.current_stack[n][:]
                    self.current_stack[n].clear()
        #self.stack_list[n].sort(key=lambda i: len(i))
        #self.div_dict[n] = self.stack_list[n] #[-1]
        return self.div_dict[n] #[-1]

    @staticmethod
    def verify_sum(N, lst):
        sum = 1
        for a, _ in enumerate(lst):
            sum *= lst[-(a + 1)]
            sum += 1
        return N == sum - 1

    @staticmethod
    def reference_examples(file_path):
        pattern0 = r'^N = (\d+)'
        pattern1 = r'Divisors = ([\d,]+)'
        number_ref = div_str_ref = None
        res_ref = []
        for line in open(file_path):
            m0 = re.search(pattern0, line)
            m1 = re.search(pattern1, line)
            if m0:
                number_ref = m0[1]
            if m1:
                div_str_ref = m1[1]
            if number_ref and div_str_ref:
                res_ref.append([int(number_ref), [int(x) for x in (div_str_ref.split(','))]])
                number_ref = div_str_ref = None
        return res_ref


aab_issue = AAB_issue()
# print(aab_issue.find_aab_factors(1000000000000))
ref_res = aab_issue.reference_examples(examples_path)
for a in ref_res:
    print("For {}:".format(a[0]))
    res_list = verify_func(aab_issue.find_aab_factors, a[0])
    print("\tSelf verification of the sum: {}".format(aab_issue.verify_sum(a[0], res_list)))
    print("\tFactor qty verification: {}".format(
          len(a[1]) == len(res_list)))
    aab_issue.div_dict.clear()

