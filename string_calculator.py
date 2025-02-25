import re


class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "": 
            return 0

        delimiters = [',', ';', '\n']

        # Handle different delimiters
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            delimiters.append(parts[0][2:])  # Extract custom delimiter
            numbers = parts[1]  # Remove the delimiter definition
        
        pattern = '|'.join(map(re.escape, delimiters))  # Regex split
        num_list = re.split(pattern, numbers)
        return sum(map(int, num_list))
        
        
