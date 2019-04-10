import os, sys, requests

def generate_todo():
    for name in os.listdir('./'):
        if name.find('.py') != -1:
            with open(name, 'r') as f:
                lines = f.readlines()
                for x in range(len(lines)):
                    name_line = ''
                    desc_line = ''
                    if lines[x] != '\n':
                        if lines[x].find('#TODO') != -1:
                            starting_pos = x
                            while x != len(lines) and lines[x].find('#') != -1:
                                limit = 0
                                if x == len(lines) - 1:
                                    limit = len(lines[x])
                                else:
                                    limit = len(lines[x])-1
                                if x != starting_pos:
                                    desc_line = desc_line + lines[x][1:limit]
                                else:
                                    name_line = name_line + lines[x][1:limit]
                                x = x + 1
                            write_to_readme(f"{name_line[5:]} ({name}, L{x})")
                            write_to_trello(f"{name_line[5:]} ({name}, L{x})", desc_line)
                        
def write_to_readme(line):
    text = ''
    with open('README.md', 'r') as f:
        text = f.read()
    if text.find(line[:line.rindex(',')]) != -1 and text.find(line) == -1:
        line_start_index = len(line[:line.rindex(',')])
        line_end_index = len(line)
        text_start_index = text.index(line[:line.rindex(',')]) + line_start_index
        text_end_index = text.index(line[:line.rindex(',')]) + line_end_index
        final_text = text[:text_start_index] + line[line_start_index:line_end_index] + text[text_end_index:]
        with open('README.md', 'w') as f:
            f.write(final_text)
    elif text.find(line) == -1:
        index = text.index('Todo:') + 6
        final_text = f'{text[:index]}* {line}\n{text[index:]}'
        with open('README.md', 'w') as f:
            f.write(final_text)

def write_to_trello(name_line, desc_line):
    url = "https://api.trello.com/1/lists/5cae4d60dbc72e1b0dab55fc/cards"
    querystring = {"key":"bc17056adfaa55d52c845b6754c3c696","token":sys.argv[1]}
    response = requests.request("GET", url, params=querystring)
    card_already_present = False
    card_needs_replaced = False
    card_id = ''
    for x in range(len(response.json())):
        if name_line == response.json()[x]['name']:
            card_already_present = True
        elif name_line != response.json()[x]['name'] and name_line[:name_line.rindex(',')] == response.json()[x]['name'][:name_line.rindex(',')]:
            card_needs_replaced = True
            card_id = response.json()[x]['id']

    if card_needs_replaced:
        print('Updating trello card...')
        url = f'https://api.trello.com/1/cards/{card_id}'
        querystring = {"name":name_line,"key":"bc17056adfaa55d52c845b6754c3c696","token":sys.argv[1]}
        response = requests.request("PUT", url, params=querystring)
    elif not card_already_present:
        print('Creating trello card...')
        url = "https://api.trello.com/1/cards"
        querystring = {"idList":"5cae4d60dbc72e1b0dab55fc","keepFromSource":"all","name":name_line,"desc":desc_line,"key":"bc17056adfaa55d52c845b6754c3c696","token":sys.argv[1]}
        response = requests.request("POST", url, params=querystring)


print('Starting python script...')
generate_todo()
print('Finished python script!')