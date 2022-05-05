import string

def read_in_chunks(file_object, chunk_size=256):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

def read_file(filename,from_line_num,to_line_num):
    upper_case_count, sent_count, para_count, line_nums, lines,sent_chs = 0, 0, 1, 0, [], (' ','\n')
    with open(filename) as f:
        line = ""
        for piece in read_in_chunks(f):
            for i,ch in enumerate(piece):
                if (from_line_num-1)<=line_nums<=(to_line_num-1):
                    line+=ch
                if ch in string.ascii_uppercase:
                    upper_case_count+=1
                if ch in sent_chs and piece[i-1] == '.':
                    sent_count+=1
                if ch == '\n' and piece[i-1] == '\n':
                    paras += 1
                if ch == '\n':
                    line_nums+=1
                    if line:
                        lines.append(line)
                    line=""
    return({"upper_case_count":upper_case_count, "sent_count": sent_count, 'para_count':para_count, 'selected_lines': ''.join(lines)})
