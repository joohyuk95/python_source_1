import cv2


class Filter: # F = Filter(), F.applyFilter(img), F.setFilter(text)
    def __init__(self):
        self.currentFilter = "original"     # 문자열 저장할 멤버 변수 기본값 = original

    def applyFilter(self, img):             # 이미지를 인자로 받아서 필터 씌워서 반환
        if self.currentFilter == "orginal":
            return img

        elif self.currentFilter == "blur":  # 멤버 변수의 문자열에 따라 분기
            return cv2.blur(img, (5, 5))

        elif self.currentFilter == "medianBlur":
            return cv2.medianBlur(img, 5)

        elif self.currentFilter == "Gaussianbur":
            return cv2.GaussianBlur(img, (5, 5), 0)

        elif self.currentFilter == "threshold":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # 원본영상은 칼라
            ret, retImg = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            return retImg

        elif self.currentFilter == "Sobel":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, retImg = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            result = cv2.Sobel(retImg, cv2.CV_64F, 1, 0, ksize=3)
            return cv2.convertScaleAbs(result)

        elif self.currentFilter == "Laplacian":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, retImg = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            result = cv2.Laplacian(retImg, cv2.CV_64F, ksize=3)
            return cv2.convertScaleAbs(result)

        elif self.currentFilter == "reverse":
            return ~img

        else:
            return img

    def setFilter(self, text):      # F.setFilter('Sobel') 원하는 필터 텍스트로 설정
        self.currentFilter = text