def string_sort(array):

    if len(array) <= 1:
        return array

    pivot = array[0]
    left = ""
    right = ""

    for element in array[1:]:
        if element < pivot:
            left += element

    for element in array[1:]:
        if element >= pivot:
            right += element
    
    return string_sort(left) + pivot + string_sort(right)


def is_anagram(first_string: str, second_string: str):
    if first_string != "" or second_string != "":
        first_string_sorted = string_sort(first_string.lower())
        second_string_sorted = string_sort(second_string.lower())
        anagram_checker = first_string_sorted == second_string_sorted

        return first_string_sorted, second_string_sorted, anagram_checker

    return first_string, second_string, False
