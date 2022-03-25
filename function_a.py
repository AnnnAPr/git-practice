def most_common_value(number_list):
    """ returns the most common element of the list
    """
    most_common_value = {}
    for num in number_list:
        if not num in most_common_value:
            most_common_value["num"] = 1
        else:
            most_common_value["num"] += 1

    max_value = 0
    for key, value in most_common_value:
        if value >= max_value:
            max_value = value
            return key



if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
