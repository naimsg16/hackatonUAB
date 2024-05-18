def check_comment (line):
        for token in line:
            if( '#' in token):
                content = token.split('#')
                print(content)
                code = content[0]
                comment = content[1]
                file2.write(f"{code} # {comment.upper()} \n")


if __name__=="__main__":            
    with open("prova.py","r") as file:
        lines = file.readlines()
    
    with open("output.py","a") as file2:
        file2.truncate(0)
        for line in lines:
            tokenized =  line.split('\n')
            check_comment(tokenized)




