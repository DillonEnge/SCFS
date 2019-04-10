import os

def generate_todo():
    for name in os.listdir('./'):
        if name.find('.py') != -1:
            with open(name, 'r') as f:
                lines = f.readlines()
                for x in range(len(lines)):
                    todo_line = ''
                    if lines[x] != '\n':
                        if lines[x].find('#TODO') != -1:
                            while x != len(lines) and lines[x].find('#') != -1:
                                limit = 0
                                if x == len(lines) - 1:
                                    limit = len(lines[x])
                                else:
                                    limit = len(lines[x])-1
                                todo_line = todo_line + lines[x][1:limit]
                                x = x + 1
                            write_to_readme(f"{todo_line[5:]} ({name}, L{x})")
                        
def write_to_readme(line):
    text = ''
    with open('README.md', 'r') as f:
        text = f.read()
    if text.find(line) == -1:
        index = text.index('Todo:') + 6
        final_text = text[:index] + '* ' + line + '\n' + text[index:]
        with open('README.md', 'w') as f:
            f.write(final_text)


print('Starting python script...')
generate_todo()
print('Finished python script!')