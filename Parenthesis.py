class CorrectParentheses:
    def find_longest_correct_parentheses(self, in_str: str) -> int:
        tmp_list = []
        max_len = 0
        for c in in_str:
            if c == '(':
                tmp_list.append(-1)
            elif c == ')' and len(tmp_list) > 0:
                if tmp_list[-1] == -1:
                    if 0 < len(tmp_list) - 1 and tmp_list[-2] > 0:
                        tmp_list.pop()
                        tmp_list[-1] = tmp_list[-1] + 1
                    else:
                        tmp_list[-1] = 1
                elif len(tmp_list) - 1 > 0 and tmp_list[-1] > 0 and tmp_list[-2] == -1:
                    a = tmp_list.pop()
                    tmp_list[-1] = a + 1
                else:
                    tmp_list.append(0)
                if len(tmp_list) > 1 and tmp_list[-1] > 0 and tmp_list[-2] > 0:
                    a = tmp_list.pop()
                    tmp_list[-1] = tmp_list[-1] + a
                max_len = max(max_len, tmp_list[-1])

        return max_len * 2


if __name__ == "__main__":
    parentheses_obj = CorrectParentheses()
    print("The length of the longest parentheses string is ",
          parentheses_obj.find_longest_correct_parentheses(input("Enter a string with parentheses: ")))
