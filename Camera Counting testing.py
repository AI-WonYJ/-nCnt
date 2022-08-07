import cv2
import numpy as np
from time import sleep

largura_min=130 # 최소 직사각형 너비
altura_min=130 # 직사각형의 최소 높이

offset=6 # 픽셀 간 허용 오차

pos_linha=300 # 카운트 라인 위치

delay= 60 # 비디오 fps

detec = []
carros= 0

	
def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

cap = cv2.VideoCapture(0) # 웹캠 열기
subtracao = cv2.bgsegm.createBackgroundSubtractorMOG() # 배경 제거

while True:
    ret , frame1 = cap.read() # 웹캠 읽어오기
    tempo = float(1/delay) # 프레임 설정
    sleep(tempo) 
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY) # BGR을 그레이 스케일로 변경
    blur = cv2.GaussianBlur(grey,(3,3),5) # Gaussian 흐림 효과를 설정
    img_sub = subtracao.apply(blur) # 배경 제거한 영상에 Gauusian 흐림 효과 적용
    dilat = cv2.dilate(img_sub,np.ones((5,5))) # 이미지 팽창, 글씨, 사물 이미지 등을 굵게 표시해 뚜렷하게 만든다.
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)) # 구조 요소 생성 (커널의 형태, 커널의 크기, 중심점)
    dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel) # 모폴리지 연산 함수, (원본 배열, 연산 방법, 구조 요소, 고정점, 반복 횟수, 테두리 외삽법, 테두리 색상)
    dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    contorno, h = cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # 외곽선 검출 함수, (입력 영상, 외곽선 검출 모드, 외곽선 근사화 방법, 검출된 외곽선 좌표, 외곽선 계층 정보, 좌표 값 이동 옵셋)
    
    cv2.line(frame1, (0, pos_linha), (1200, pos_linha), (255,127,0), 3)  # 카운트 라인 그리기 (이미지 파일, 시작점 좌표 (x, y), 종료점 좌표 (x, y), 색상 (blue, green, red), 선 두께, 선 종류, fractional bit)
    for(i,c) in enumerate(contorno): # 카운트 라인에 닿았을 때
        (x,y,w,h) = cv2.boundingRect(c) # 주어진 점을 감싸는 최소 크기 사각형(바운딩 박스)를 반환한다.
        validar_contorno = (w >= largura_min) and (h >= altura_min) # 직사각형 최소 높이, 너비와 비교
        if not validar_contorno:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2) # 사각형 그리기, (이미지 파일, 시작점 좌표 (x, y), 종료점 좌표 (x, y), 색상 (blue, green, red), 선 두께, 선 종류, fractional bit)
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 0,255), -1) # 원 그리기

        for (x,y) in detec:
            if y<(pos_linha+offset) and y>(pos_linha-offset): # 카운트 라인 안에 들어올 때
                carros+=1 # 카운트 값 증가
                cv2.line(frame1, (0, pos_linha), (1200, pos_linha), (0,127,255), 3) # 선 색상 변경
                detec.remove((x,y)) # 초기화
                print("car is detected : "+str(carros)) # 카운트 출력
       
    cv2.putText(frame1, "VEHICLE COUNT : "+str(carros), (0, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255),3) # 텍스트 출력, (이미지 파일, 출력 문자, 출력 문자 시작 위치 좌표 (좌측 하단), fontFace,  폰트 크기, 폰트 색상, 폰트 두께, 선 종류, org 사용 옵션 (True: 좌측 하단, False: 좌측 상단))
    cv2.imshow("Video Original" , frame1) # 카메라 영상 출력
    cv2.imshow("Detectar",dilatada) # 회색 카메라 영상 출력

    if cv2.waitKey(1) == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
