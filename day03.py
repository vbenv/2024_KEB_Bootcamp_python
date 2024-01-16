#예외 발생 시 대처
subjects = "python c++ database linux"
subject = input("수강신청과목 입력 : ")

try:
    print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다.")
except ValueError:
    print('해당 과목이 존재하지 않습니다.')

print(subjects[subjects.find(subject)])
#Q.subjects에 없는 과목 입력하면 에러가 뜬다는 데 안 뜸
if subjects.find(subject) != -1:
    print("있습니다")
else:
    print("없습니다.")