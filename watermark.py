import cv2
import math
import numpy as np


class Watermark:
    def __init__(self, text='Sample watermark', alpha=0.3, color=(0, 0, 255)):
        self.text = text if text[-1] == ' ' else text + ' '
        self.alpha = alpha
        self.reverse_alpha = 1 / (1 - self.alpha)
        self.reverse_gamma = 1 - (1 / (1 - self.alpha))
        self.color = color
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 0.7
        self.thickness = 2
        self.text_width, self.text_height = cv2.getTextSize(text, self.font, self.font_scale, self.thickness)[0]
        self.image = []

    def __get_line_text(self):
        line = ''
        for i in range(math.ceil(self.text_width)):
            line += self.text
        return line

    def __read_image(self, image_path):
        self.image = cv2.imread(image_path, -1)

    def __create_transparent_mat(self):
        return np.zeros((self.image.shape[0], self.image.shape[1], 4), dtype=self.image.dtype)

    def add_watermark(self, image_path):
        self.__read_image(image_path)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2BGRA)
        zeros = self.__create_transparent_mat()
        text_to_print = self.__get_line_text()
        y_cord = self.text_height
        while y_cord <= self.image.shape[0] + self.text_height:
            cv2.putText(zeros, text_to_print, (0, y_cord), self.font, self.font_scale, self.color, self.thickness)
            y_cord += self.text_height * 2
        watermarked_image = cv2.addWeighted(zeros, self.alpha, self.image, 1, 0)
        return watermarked_image

    def remove_watermark(self, image_path):
        self.__read_image(image_path)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2BGRA)
        zeros = self.__create_transparent_mat()
        text_to_print = self.__get_line_text()
        y_cord = self.text_height
        while y_cord <= self.image.shape[0] + self.text_height:
            cv2.putText(zeros, text_to_print, (0, y_cord), self.font, self.font_scale, self.color, self.thickness)
            y_cord += self.text_height * 2
        un_watermarked_image = cv2.addWeighted(self.image, self.reverse_alpha, zeros, self.reverse_gamma, 0)
        return un_watermarked_image
