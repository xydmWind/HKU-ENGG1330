def cut_cable(total_length: int, piece_length: int):
    return total_length // piece_length, total_length % piece_length


total_length = int(input())
piece_length = int(input())
print(cut_cable(total_length, piece_length))