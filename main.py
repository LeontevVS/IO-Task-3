def union_files():
    path1 = r"files/1.txt"
    path2 = r"files/2.txt"
    path3 = r"files/3.txt"
    with open(path1, 'rt', encoding='utf-8') as file1, open(path2, 'rt', encoding='utf-8') as file2, open(path3, 'rt', encoding='utf-8') as file3, open('files/result.txt', 'wt', encoding='utf-8') as file_result:
        files = [file1, file2, file3]
        sorted_files = []
        for file in files:
            file_info = {}
            file_info['name'] = file.name
            file_info['lines'] = file.readlines()
            file_info['lines_count'] = len(file_info['lines'])
            sorted_files.append(file_info)
        sorted_files.sort(key=lambda x: x['lines_count'])
        for file in sorted_files:
            file_result.write(f'{file["name"]}\n{file["lines_count"]}\n')
            file_result.writelines(file['lines'])
            file_result.write('\n')

if __name__ == "__main__":    
    union_files()
