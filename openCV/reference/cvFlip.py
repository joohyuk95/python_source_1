import cv2

class Flip:

    def __init__(self):
        self.currentImg = "case0"
    
    def applyFlip(self, img):
        if self.currentImg == "case0":
            return img
        
        elif self.currentImg == "case1":
            return cv2.flip(img, 1)

        elif self.currentImg == "case2":
            return cv2.flip(img, 0)

        else:
            return cv2.flip(cv2.flip(img, 0), 1)
            
    def setFlip(self, text):
        self.currentImg = text