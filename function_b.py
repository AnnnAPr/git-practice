# Taken From
# Iterating Over Data
# Problem-Set While Loops #11

def silly_sum():
    """ reads numbers from the user (use input_int) 
        summing as we go until either
        the user enters 0, or
        the sum reaches or exceeds 1000
    """
    sum = 0
    while sum < 1000:
        new_number = int(input("Type in a number to add: "))
        if new_number == 0:
            break
        sum += new_number
    
    return sum

if __name__ == "__main__":
    print(f"Answer = {silly_sum()}")
