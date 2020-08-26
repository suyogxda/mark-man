import os
import cv2
import math
import time
import errno
import numpy as np


class Watermark:
    def __init__(self, text='Sample watermark', alpha=0.3, color=(0, 0, 255), path_to_save='./result'):
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
        self.save_path = path_to_save

    def __create_save_directory(self):
        try:
            print("Creating directory `{}`".format(self.save_path))
            os.makedirs(self.save_path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
            else:
                print("Directory: `{}` already exists in current path.....skipping")

    def __get_line_text(self):
        line = ''
        for i in range(math.ceil(self.text_width)):
            line += self.text
        return line

    def __read_image(self, image_path):
        self.image = cv2.imread(image_path, -1)

    def __create_transparent_mat(self):
        return np.zeros((self.image.shape[0], self.image.shape[1], 4), dtype=self.image.dtype)

    def __write_image(self, image):
        self.__create_save_directory()
        save_name = os.path.join(self.save_path, time.strftime("%Y%m%d-%H%M%S") + ".png")
        cv2.imwrite(save_name, image)
        print("Image saved as `{}`".format(save_name))

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
        print("Successfully added watermark")
        self.__write_image(watermarked_image)
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
        print("Successfully removed watermark")
        self.__write_image(un_watermarked_image)
        return un_watermarked_image
