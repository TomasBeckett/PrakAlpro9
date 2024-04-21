# LATIHAN 8.1

with open('SOAL-1/teks1.txt', 'r') as file1, open('SOAL-1/teks2.txt', 'r') as file2:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

    max_lines = max(len(lines1), len(lines2))

    for line in range(max_lines):
        line1 = lines1[line].strip() if line < len(lines1) else ''
        line2 = lines2[line].strip() if line < len(lines2) else ''
        
        if line1 != line2:
            print(f'Perbedaan baris {line + 1}:')
            print(f'File 1: {line1}')
            print(f'File 2: {line2}')
            print()

