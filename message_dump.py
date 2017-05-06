import time

import groupy


def get_group_by_name(group_list, name):
    for g in group_list:
        if g.name == name:
            return g
    return None

if __name__ == '__main__':
    GROUP_NAME = 'GROUP_NAME'
    groups = groupy.Group.list()
    group = get_group_by_name(groups, GROUP_NAME)
    messages = group.messages()

    try:
        while messages.iolder():
            print("iteration")
            time.sleep(0.1)
    except:
        pass

    if len(messages) == group.message_count:
        print("Successfully downloaded messages.")

    with open('output.html', 'w') as fout:
        fout.write('<html>\n')
        fout.write(GROUP_NAME)
        fout.write(' from ')
        fout.write(str(messages.last.created_at))
        fout.write(' to ')
        fout.write(str(messages.first.created_at))
        fout.write(':\n')
        fout.write('<table>\n')
        fout.write('<tr>')
        fout.write('<th>')
        fout.write('Date')
        fout.write('</th>')
        fout.write('<th>')
        fout.write('Name')
        fout.write('</th>')
        fout.write('<th>')
        fout.write('Message')
        fout.write('</th>')
        fout.write('</tr>\n')
        for message in reversed(messages):
            fout.write('<tr>')
            fout.write('<td>')
            fout.write(str(message.created_at))
            fout.write('</td>')
            fout.write('<td>')
            fout.write(str(message.name))
            fout.write('</td>')
            fout.write('<td>')
            if message.text:
                fout.write(str(message.text))
            for attachment in message.attachments:
                try:
                    fout.write('<a href="')
                    fout.write(str(attachment.url))
                    fout.write('">Attachment</a>')
                except AttributeError:
                    pass
            fout.write('</td>')
            fout.write('</tr>\n')
        fout.write('</table>\n')
        fout.write('</html>\n')
