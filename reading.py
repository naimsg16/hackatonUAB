def check_comment (token):
    if( '#' in token):
        content = token.split('#')
        code = content[0]
        comment = content[1]
        file2.write(f"{code}#{comment.upper()} \n")
    elif token != '':
        file2.write(token + '\n')
    else:
        file2.write('\n')


if __name__=="__main__":
    toggle = False         
    with open("prova.py","r", encoding="utf-8") as file:
        lines = file.readlines()
    with open("output.py","a", encoding="utf-8") as file2:
        file2.truncate(0)
        for line in lines:
            tokenized =  line.split('\n')
            if tokenized[0] == "\"\"\"":
                file2.write("\"\"\"\n")
                toggle = not toggle
            elif toggle:
                file2.write(tokenized[0].upper() + '\n')
            else:
                check_comment(tokenized[0])