class Solution:
    def defangIPaddr(self, address: str) -> str:
        numbers = address.split('.')
        new_string = '[.]'.join(numbers)
        return new_string