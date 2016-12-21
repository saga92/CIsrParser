#-----------------------------------------------------------------
# pycparser: func_write.py
#
# Tiny example of rewriting a AST node
#
# Copyright (C) 2014, Akira Hayakawad
# License: BSD
#-----------------------------------------------------------------
from __future__ import print_function
import sys

from pycparser import c_parser

text = r"""
void func(void)
{
  x = 1;
}

int y=0;
"""

parser = c_parser.CParser()
ast = parser.parse(text)
print("Before:")
ast.show(offset=2)

assign = ast.ext[0].body.block_items[0]
assign.lvalue.name = "y"
assign.rvalue.value = 2
#assign.op = "+="
#print(type(ast.ext[0].body.block_items[0].lvalue))
#print(type(ast.ext[1]))
print(dir(ast.ext[1]))
print(ast.ext[1].__class__)
print(ast.ext[1].__delattr__)
print(ast.ext[1].__doc__)
print(ast.ext[1].__format__)
print(ast.ext[1].__getattribute__)
print(ast.ext[1].__hash__)
print(ast.ext[1].__init__)
print(ast.ext[1].__module__)
print(ast.ext[1].__new__)
print(ast.ext[1].__reduce__)
print(ast.ext[1].__reduce_ex__)
print(ast.ext[1].__repr__)
print(ast.ext[1].__setattr__)
print(ast.ext[1].__sizeof__)
print(ast.ext[1].__slots__)
print(ast.ext[1].__str__)
print(ast.ext[1].__subclasshook__)
print(ast.ext[1].__weakref__)
print(ast.ext[1].attr_names)
print(ast.ext[1].children)
print(ast.ext[1].coord)
print(ast.ext[1].name)
print(ast.ext[1].quals)
print(ast.ext[1].storage)
print(ast.ext[1].funcspec)
print(ast.ext[1].type)
print(ast.ext[1].init)
print(ast.ext[1].bitsize)

print("After:")
#ast.show(offset=2)
ast.show()
