import sys
input = sys.stdin.readline

gpa_table = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}

total_credit = 0
total_gpa = 0
for _ in range(20):
    lecture, credit, gpa = input().split()
    if gpa == 'P':
        continue
    total_credit += float(credit)
    total_gpa += float(credit) * gpa_table[gpa]
print(f'{total_gpa / total_credit:.6f}')
