class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        i = 0
        self.result += num
        if len(nums) > 0:
            while i < len(nums):
                self.result += nums[i]
                i += 1
        return self

    def subtract(self, num, *nums):
        i = 0
        self.result -= num
        if len(nums) > 0:
            while i < len(nums):
                self.result -= nums[i]
                i += 1
        return self


# create an instance:
md = MathDojo()
# to test:
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
# run each of the methods a few more times and check the result!
