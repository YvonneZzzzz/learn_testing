#!/usr/bin/env python
# -*- coding: utf-8 -*-

from count import A

class B(A):

     def sub (self,a, b):
         return a - b

resule = B().add(2, 5)
print(resule)