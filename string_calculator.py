class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "": 
            return 0

        num_list = numbers.split(",") # splitting the string by comma  into array  and adding the items in array.
        return sum(map(int, num_list))
        
        
