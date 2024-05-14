# -*- coding: utf-8 -*-
"""
Created on Tue May 14 10:45:31 2024

@author: ocanh
"""

class p9e2:
    @staticmethod
    def methodtambah(x, y=None):
        if y is None:
            return x
        elif isinstance(x, int) and isinstance(y, int):
            return x + y
        elif isinstance(x, float) and isinstance(y, float):
            return x + y
        else:
            raise ValueError("Tipe data tidak didukung")

mynum1 = p9e2.methodtambah(8, 5)
mynum2 = p9e2.methodtambah(4.5, 6.5)
print('int:', mynum1)
print('float:', mynum2)
