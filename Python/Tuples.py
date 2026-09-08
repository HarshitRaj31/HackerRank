if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    input_tuples=tuple(integer_list)
    print(hash(input_tuples))
