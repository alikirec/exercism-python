from bdb import effective
import re


def grep(pattern, flags, files):
    multiple_files = len(files) > 1

    print_line_numbers = '-n' in flags
    print_only_file_name = '-l' in flags
    match_whole_line = '-x' in flags
    inverted = '-v' in flags

    effective_pattern = pattern
    re_flags = 0
    if '-i' in flags:
        # case insensitive
        re_flags |= re.I
    if match_whole_line:
        effective_pattern = f'^{pattern}$'

    prog = re.compile(effective_pattern, re_flags)

    result = []
    for file_name in files:
        file = open(file_name)
        line_no = 0
        for line in file:
            line_no += 1
            match = prog.search(line)
            if (match and not inverted) or (not match and inverted):
                if print_only_file_name:
                    result.append(file_name)
                    break

                line_to_append = line
                if line_to_append.endswith('\n'):
                    # strip new line as they are gonna be joined
                    line_to_append = line_to_append[:-1]
                if print_line_numbers:
                    line_to_append = f'{line_no}:{line_to_append}'
                if multiple_files:
                    line_to_append = f'{file_name}:{line_to_append}'

                result.append(line_to_append)

    return "\n".join(result) + ("\n" if result else "")
