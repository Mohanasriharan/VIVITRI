# -*- coding: utf-8 -*-
"""Question 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DnyymX0flvBEx5Y2vycB7_L9uNJg_WSS
"""

def main():
    s = "learn programming at include help"
    k = 6
    l = s.split()
    for i in l:
        if len(i) > k:
            print(i, end=" ")



if __name__ == '__main__':
    main()

