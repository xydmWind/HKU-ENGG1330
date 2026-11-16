def collect_labels(item):
    if isinstance(item, str):
        return [item]
    result = []
    for i in item:
        result = result + collect_labels(i)
    return result


from ast import literal_eval

item = literal_eval(input())
print(collect_labels(item))
print(item)