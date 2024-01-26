class Solution:
    def swap_two_numbers(self, a, b):

        if a == 0:
            a = b
            b = 0
            print("a =", a)
            print("b =", b)
            return
        if b == 0:
            b = a
            a = 0
            print("a =", a)
            print("b =", b)
            return
        else:
            a = a * b
            b = a / b
            a = a / b
            print("a =", a)
            print("b =", b)


if __name__ == "__main__":
    solution = Solution()
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    solution.swap_two_numbers(a, b)
