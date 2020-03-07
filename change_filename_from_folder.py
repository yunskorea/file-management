# -*- coding: utf-8 -*-

import sys  # 실행시 파라미터 입력
import os   # 파일명 변경

# path_start = "./test"
print('arg1:', sys.argv[1])
path_start = sys.argv[1]     # 시작 디렉토리 위치


# 디렉토리 반복
for path, dirs, files in os.walk(path_start):

    print('-' * 30)

    # 파일명에 번호 추가하기 초기값
    file_num = 0

    # 디렉토리 안의 파일 갯수만큼 반복
    for file in files:
        # 디렉토리+파일명 출력
        print (os.path.join(path, file))
        print('path:', path)
        print('file:', file)

        # 폴더명만 추출
        if(path.find('\\')) > 0 :
            foldername1 = path.split('\\')[-1]  # 윈도우 환경
        else :
            foldername1 = path.split('/')[-1]  # 리눅스 환경
        print('foldername1:', foldername1)


        # 기존 파일명 출력
        print('old_filename:', file)

        # 파일명에 붙일 숫자에 1씩 증가
        file_num += 1

        # 파일명에서 확장자 추출
        file_extension = file.split('.')[-1]    # 파일 확장자

        # 파일명을 제목 + 일련번호로 바꾸기
        new_filename = foldername1 + "_" + str(file_num) + "." + file_extension
        # 새로운 파일명 출력
        print('new_filename:', new_filename)

        # print('old_path:', os.path.join(path, file))
        # print('new_path:', os.path.join(path, new_filename))
        # 파일명 변겅 처리
        os.rename(os.path.join(path, file), os.path.join(path, new_filename))
