import cv2
import sys
import math
import numpy as np


class Watermark:
    def __init__(self, text='Sample watermark', alpha=0.3, color=(0, 0, 255)):
        self.text = text if text[-1] == ' ' else text + ' '
        self.alpha = alpha
        self.color = color
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 0.7
        self.thickness = 1
        self.text_width, self.text_height = cv2.getTextSize(text, self.font, self.font_scale, self.thickness)[0]
        self.image = []

    def __get_line_text(self):
        line = ''
        for i in range(math.ceil(self.text_width)):
            line += self.text
        return line

    def __read_image(self, image_path):
        self.image = cv2.imread(image_path, -1)

    def add_watermark(self, image_path):
        self.__read_image(image_path)
        text_to_print = self.__get_line_text()
        y_cord = self.text_height
        while y_cord <= self.image.shape[0] + self.text_height:
            cv2.putText(self.image, text_to_print, (0, y_cord), self.font, self.font_scale, self.color, self.thickness)
            y_cord += self.text_height * 2
        return self.image


if __name__ == '__main__':
    alakazam = Watermark()
    cv2.imshow("Alakazam", alakazam.add_watermark(sys.argv[1]))
    cv2.waitKey()
