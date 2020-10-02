def handle_uploaded_file(f):
    with open('media/CAD/tool_list/cnc_uploaded.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return destination


def tool_list(f):
    # 'This function will extract all tool numbers that are used in CNC program')
    # 'Program will generate tool list file that can be used to measure tools length on CNC machine')
    tool_set = set()
    try:
        uploaded_file = handle_uploaded_file(f)
        with open(uploaded_file.name, 'r') as file:
            cnc_file = file.readlines()
    except FileNotFoundError:
        print('File not found!')
    for cnc_line in cnc_file:
        tool_change = cnc_line.find('M6')
        if tool_change != -1:
            tool_no = cnc_line.split('M6')[0].strip()
            if tool_no == "T200" or tool_no == "T999":
                continue
            tool_set.add(tool_no)
    tool_list_sorted = sorted(list(tool_set))
    tool_list_file = 'static/CAD/TOOL_LIST.MIN'
    with open(tool_list_file, 'w') as file:
        for tool in tool_list_sorted:
            file.write(f'{tool} M6\n')
            file.write(f'M1\n')
            file.write(f'G119\n')
        file.write('M2\n')
        file.write('%')
