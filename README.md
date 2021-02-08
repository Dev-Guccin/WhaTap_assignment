# WhaTap_assignment

## 파일 설명
* target.txt : 모니터링 할 프로세스가 존재 ex) nginx\n
* columns.txt : csv를 출력할때 뽑고자 하는 columns들이 존재 ex) CMD1,CMD2,PID,PPID
* monitoring.py : 모니터링을 진행하는 코드
* static.csv : 모니터링한 결과가 저장된 csv파일

## 사용법
1. 모니터링할 프로세스의 이름을 target.txt에 입력한다. ex) nginx
2. csv로 뽑고자 하는 columns들을 columns.txt에 입력한다. ex) CMD1,CMD2,PID,PPID
3. python3 monitoring.py를 실행하여 모니터링을 시작한다.
4. static.csv를 확인하여 모니터링 결과를 확인한다.
