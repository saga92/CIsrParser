#-------------------------------------------------------------------------------
# pycparser: using_gcc_E_libc.py
#
# Similar to the using_cpp_libc.py example, but uses 'gcc -E' instead
# of 'cpp'. The same can be achieved with Clang instead of gcc. If you have
# Clang installed, simply replace 'gcc' with 'clang' here.
#
# Copyright (C) 2008-2015, Eli Bendersky
# License: BSD
#-------------------------------------------------------------------------------
import sys

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])

from pycparser import parse_file


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename  = sys.argv[1]
    else:
        filename = 'examples/c_files/year.c'

    ast = parse_file(filename, use_cpp=True,
            cpp_path='gcc',
            cpp_args=['-E', r'-Iutils/fake_libc_include'])
    ast.show()
    print ("\033[1;5;32;45;1msimulate\033[0m")
    print(ast.ext[169])                                     #FuncDef
    print(ast.ext[169].decl)                                #Decl
    print(ast.ext[169].decl.name)                           #simulate
    print(ast.ext[169].decl.quals)                          #[]
    print(ast.ext[169].decl.storage)                        #[]
    print(ast.ext[169].decl.funcspec)                       #[]
    print(ast.ext[169].decl.type)                            #FuncDecl
    print(ast.ext[169].decl.type.args)                       #None
    print(ast.ext[169].decl.type.type)                      #TypeDecl
    print(ast.ext[169].decl.type.type.declname)                   #simulate
    print(ast.ext[169].decl.type.type.quals)                      #[]
    print(ast.ext[169].decl.type.type.type)                      #IdentifierType
    print(ast.ext[169].decl.type.type.type.names)                      #['void']     a list
    print(ast.ext[169].decl.init)
    print(ast.ext[169].decl.bitsize)

    print ("\033[1;5;32;45;1mext[169].body\033[0m")
    print(ast.ext[169].body.block_items[3])
    print(ast.ext[169].body.block_items[3].name)
    print(ast.ext[169].body.block_items[3].quals)
    print(ast.ext[169].body.block_items[3].storage)
    print(ast.ext[169].body.block_items[3].funcspec)
    print(ast.ext[169].body.block_items[3].type)
    print(ast.ext[169].body.block_items[3].init)
    print(ast.ext[169].body.block_items[3].bitsize)