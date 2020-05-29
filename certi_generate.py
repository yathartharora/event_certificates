import cv2 as cv
from datetime import date

class certificateGenerator:
    
    def generate_certificate(self,certi_path,logo_path,participant_name,event_name,organiser_name,issuer_name):
        s_img = cv.imread(logo_path,cv.IMREAD_UNCHANGED)
        l_img = cv.imread(certi_path)
        resize_img = cv.resize(s_img,(150,150))
        x_offset=120
        y_offset=60
        font_size = 3
        font = cv.FONT_HERSHEY_PLAIN
        font_color = (0,0,0)
        l_img[y_offset:y_offset+resize_img.shape[0], x_offset:x_offset+resize_img.shape[1]] = resize_img
        
        cv.putText(l_img, participant_name, (550 ,250 ), font, font_size, font_color, 2)
        cv.putText(l_img, event_name, (300 ,400 ), font, font_size, font_color, 2)
        cv.putText(l_img, organiser_name, (500 ,480 ), font, font_size, font_color, 2)
        cv.putText(l_img, issuer_name, (280 ,675 ), font, 2, font_color, 2)
        today = date.today()
        d1 = today.strftime("%B %d, %Y")
        cv.putText(l_img, d1, (820 ,670 ), font, 1, font_color, 2)
        cv.imwrite('/Users/yathartharora/test.png',l_img)
        
        
        
        
        
