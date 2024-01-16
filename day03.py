# formating
print('%s' % 42) # old version

print('%e' % 0.703)

#new version
subjects = {'python' : 'kim', 'c++' : 'sung', 'data structure' : 'kim', 'data base' : 'kang'}
print("{0[c++]} {0[data structure]}".format(subjects))  # 숫자는 인덱스 번호를 의미. 그 안에 있는 것은 키 값을 불러옴. 그 키 값에 해당하는 value값 불러옴
