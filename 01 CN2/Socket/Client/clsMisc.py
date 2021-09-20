# -*- coding: utf-8 -*-
import ctypes  # An included library with Python install.
class Misc:
    def DienTich(dai, rong=6):
        print("Diện tích là: ", dai * rong)

    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)