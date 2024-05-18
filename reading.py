def check_comment (token):
    if( '#' in token):
        content = token.split('#')
        code = content[0]
        comment = content[1]
        output.write(f"{code}#{comment.upper()} \n")
    elif token != '':
        output.write(token + '\n')
    else:
        output.write('\n')

if __name__=="__main__":
    toggle = False         
    with open("prova.py","r", encoding="utf-8") as input:
        lines = input.readlines()
    with open("output.py","a", encoding="utf-8") as output:
        output.truncate(0)
        for line in lines:
            tokenized =  line.split('\n')
            if tokenized[0] == "\"\"\"":
                output.write("\"\"\"\n") 
                toggle = not toggle
            elif toggle:
                output.write(tokenized[0].upper() + '\n')
            else:
                check_comment(tokenized[0])