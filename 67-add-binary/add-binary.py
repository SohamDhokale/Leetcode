class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            current_sum = bit_a + bit_b + carry


            result.append(str(current_sum % 2))
            carry = current_sum // 2

            i -= 1
            j -= 1

        return "".join(result[::-1])
        