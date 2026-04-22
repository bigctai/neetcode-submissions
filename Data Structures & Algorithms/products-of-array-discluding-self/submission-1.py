class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [0]*len(nums)
        right_products = [0]*len(nums)
        products = []
        for i in range(len(nums)):
            j = len(nums)-i-1
            if i == 0:
                left_products[i] = nums[i]
                right_products[j] = nums[j]
            else:
                left_products[i] = nums[i] * left_products[i-1]
                right_products[j] = nums[j] * right_products[j+1]
        for i in range(len(nums)):
            if i == 0:
                products.append(right_products[i+1])
            elif i == len(nums)-1:
                products.append(left_products[i-1])
            else:
                products.append(left_products[i-1]*right_products[i+1])
        return products
            