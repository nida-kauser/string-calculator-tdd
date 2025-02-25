import re


class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "": 
            return 0

        num_list = re.split(",|\n", numbers)  # Split by comma or newline
        return sum(map(int, num_list))
        
        
