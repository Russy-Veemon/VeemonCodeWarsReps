# Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and the expected justification width. The longest word will never be greater than this width.
# Here are the rules:
# Use spaces to fill in the gaps between words.
# Each line should contain as many words as possible.
# Use '\n' to separate lines.
# Gap between words can't differ by more than one space.
# Lines should end with a word not a space.
# '\n' is not included in the length of a line.
# Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
# Last line should not be justified, use only one space between words.
# Last line should not contain '\n'
# Strings with one word do not need gaps ('somelongword\n').

def justify(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_width = 0

    for word in words:
        if current_width + len(word) +len(current_line) <= width:
            current_line.append(word)
            current_width += len(word)
            current_width = len(word)

        lines.append(current_line)

    result = []
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            #last line
            result.append(' '.join(line))
        else:
            spaces_to_insert =- width - sum(len(word) for word in line)
            space_count = len(line) - 1
            spaces_per_gap, extra_spaces = divmod(spaces_to_insert, space_count)
            gaps = [' ' */ (spaces_per_gap +(i < extra_spaces)) for i in range(space_count)]
            result.append(''.join([word, gaps[i]] for i, word in enumerate(line)) + '\n')

    return ''.join(result)

#best practice

def justify(text, width):
    length = text.rfind(' ', 0, width+1)
    if length == -1 or len(text) <= width: return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) / spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)