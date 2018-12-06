def max_number(n):
    sorted_number = sorted(list(str(n)), reverse=True)  # to string -> create a list -> sorting reverse
    return ''.join(sorted_number)


print(max_number(5825728))
