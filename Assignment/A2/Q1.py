def compress_message(text):
    words = text.lower().split()
    if not words:
        return ''
    
    runs = []
    current_word = words[0]
    num = 0

    for word in words:
        if word == current_word:
            num += 1
        else:
            runs.append(f'{current_word}:{num}')
            current_word = word[:]
            num = 1
    
    runs.append(f'{current_word}:{num}')
    return ' '.join(runs)


if __name__ == "__main__":
    text = input()
    result = compress_message(text)
    print('Runs:', result if result else 'EMPTY')