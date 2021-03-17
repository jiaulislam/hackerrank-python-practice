from collections import namedtuple

if __name__ == "__main__":
    n = int(input())
    a = input()
    total = 0
    Student = namedtuple('Student', a)
    for _ in range(n):
        student = Student(*input().split())
        total += int(student.MARKS)
    print(f'{(total/n):.2f}')