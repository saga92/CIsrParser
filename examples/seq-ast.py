#-------------------------------------------------------------------------------
# pycparser: seq-ast.py
#
# Similar to the using_gcc_libc.py example, but add some new rules to this parser
#
# Copyright (C) 2016, Eli Ren
# License: Ren
#-------------------------------------------------------------------------------

import sys
from pycparser import c_parser, c_ast

# This is not required if you've installed pycparser into
# your site-packages/ with setup.py
#
sys.path.extend(['.', '..'])

from pycparser import parse_file, c_generator

filename = 'examples/siri/demo.seq.c'
astseq = parse_file(filename, use_cpp=True, cpp_path='gcc', cpp_args=['-E', r'-Iutils/fake_libc_include'])

def astScheDefer(id):
    schedef = c_ast.FuncCall(c_ast.ID('scheduler_deferral'),c_ast.Constant('int', id))
    # astseq.ext[166].body.block_items[6].args = c_ast.Constant('int', id)
    # schedef=astseq.ext[166].body.block_items[6]
    # print ("\033[1;5;32;45;1mFuncCall scheduler_deferral\033[0m")
    # schedef.show()
    return schedef

def astScheReg(reg):                    #the type of reg is String
    exlist=[c_ast.ID(reg)]
    exprs=c_ast.ExprList(exlist)
    rfunc=c_ast.FuncCall(c_ast.ID('scheduler_reg'),exprs)
    schereg=c_ast.Assignment('=',c_ast.ID(reg),rfunc)
    # schereg=astseq.ext[166].body.block_items[3]
    # print ("\033[1;5;32;45;1mFuncCall scheduler_deferral\033[0m")
    # schereg.lvalue.name=reg            #the type of lvalue is c_ast.ID
    # schereg.rvalue.args.exprs[0].name=reg      #the type of exprs is c_ast.ExprList and the type of exprs[0] is c_ast.ID
    # print ("\033[1;5;32;45;1m schereg.rvalue.args.exprs[0]\033[0m")
    # print(schereg.rvalue.args);
    # schereg.rvalue.args.show()
    # print ("\033[1;5;32;45;1mFuncCall scheduler_reg\033[0m")
    # schereg.show()
    return schereg

def astEnqueue(elemtype,queue):         #the type of exprs is String
    exenq=[c_ast.Constant('int', elemtype), c_ast.ID(queue)]
    exprs=c_ast.ExprList(exenq)
    enqueue=c_ast.FuncCall(c_ast.ID('Enqueue'),exprs)
    # astseq.ext[166].body.block_items[5].args.exprs[0] = c_ast.Constant('int', elemtype)
    # astseq.ext[166].body.block_items[5].args.exprs[1] = c_ast.ID(queue)
    # enqueue=astseq.ext[166].body.block_items[5]
    # print ("\033[1;5;32;45;1mFuncCall Enqueue\033[0m")
    # enqueue.show()
    return enqueue

def astScheIsr(id):
    # astseq.ext[167].body.block_items[1].name=c_ast.ID('scheduler_isr')
    # astseq.ext[167].body.block_items[1].args = c_ast.Constant('int', id)
    # print ("\033[1;5;32;45;1mastseq.ext[166].body.block_items[1]\033[0m")
    # print(astseq.ext[166].body.block_items[1])
    # print ("\033[1;5;32;45;1mastseq.ext[166].body.block_items[1].name\033[0m")
    # print(astseq.ext[166].body.block_items[1].name)
    # print ("\033[1;5;32;45;1mastseq.ext[166].body.block_items[1].args\033[0m")
    # print(astseq.ext[166].body.block_items[1].args)
    # scheisr=astseq.ext[167].body.block_items[1]
    # print ("\033[1;5;32;45;1mFuncCall scheduler_isr\033[0m")
    # scheisr.show()
    scheisr = c_ast.FuncCall(c_ast.ID('scheduler_isr'),c_ast.Constant('int', id))
    return scheisr

def astDequeue(queue):          #the type of exprs is String
    exdeq=[c_ast.ID(queue)]
    exprs=c_ast.ExprList(exdeq)
    dequeue=c_ast.FuncCall(c_ast.ID('Dequeue'),exprs)
    # astseq.ext[167].body.block_items[2].args.exprs[0] = c_ast.ID(queue)
    # dequeue=astseq.ext[167].body.block_items[2]
    # print ("\033[1;5;32;45;1mFuncCall Dequeue\033[0m")
    # dequeue.show()
    return dequeue

def astVeriNon():
    veryidt=c_ast.IdentifierType(['int'])
    verytype=c_ast.TypeDecl('rand',[],veryidt)
    bifunc=c_ast.FuncCall(c_ast.ID('__VERIFIER_nondet'),None)
    verybina=c_ast.BinaryOp('%',bifunc,c_ast.ID('N'))
    simdecl=c_ast.Decl('rand',[],[],[],verytype,verybina,None,None)
    return simdecl

def astAssiIsr(i):
    larr = c_ast.ArrayRef(c_ast.ID('isr'), c_ast.Constant('int', str(i)))  # the second param of Constant is String
    rarr = c_ast.UnaryOp('&', c_ast.ID('isr_' + str(i + 1)))
    assi = c_ast.Assignment('=', larr, rarr)
    return assi

def astAssiDef(isr):
    larr = c_ast.ArrayRef(c_ast.ID('deferral'),
                          c_ast.Constant('int', str(int(isr) - 1)))  # the second param of Constant is String
    rarr = c_ast.UnaryOp('&', c_ast.ID('deferral_' + isr))
    assi = c_ast.Assignment('=', larr, rarr)
    return assi

def astAssiPri():
    larr = c_ast.ID('pri')  # the second param of Constant is String
    rarr = c_ast.ArrayRef(c_ast.ID('prio'), c_ast.ID('rand'))
    assipri = c_ast.Assignment('=', larr, rarr)
    return assipri

def astFuncIsr():
    aray = c_ast.ArrayRef(c_ast.ID('isr'), c_ast.ID('rand'))
    funcisr=c_ast.FuncCall(aray,None)
    return funcisr


def typeName(obj):
    typeext = str(obj).split()[0].split('<')[1]
    # print[typeext]
    typeext = typeext.split('.')
    typeext = typeext[len(typeext) - 1]
    # print(typeext)
    return typeext

def isDeferral(funcname):
    fname=funcname.split('_')[0]
    # print("funcname   "+fname)
    if fname=='deferral':
        return 1
    else:
        return 0

def isHalIn(varr):
    varrname=typeName(varr)
    if varrname=='FuncCall' and varr.name.name=='HAL_IO_INPUT':
        return 1
    else:
        return 0

def isHalOut(varr):
    varrname=typeName(varr)
    if varrname=='FuncCall' and varr.name.name=='HAL_IO_OUTPUT':
        return 1
    else:
        return 0

def isIsr(funcname):
    fname=funcname.split('_')[0]
    if fname=='isr':
        return 1
    else:
        return 0


def isrDict(ast,isrdict):
    for ext in ast.ext:
        if typeName(ext) == 'FuncDef':
            funcname = ext.decl.name
            if isIsr(funcname):
                isrname = funcname.split('_')[1]
                if isrdict.has_key(isrname):
                    isrdict[isrname]=isrname
                else:
                    isrdict[isrname]=None
            elif isDeferral(funcname):
                defname = funcname.split('_')[1]
                if isrdict.has_key(defname):
                    isrdict[defname] = defname
                else:
                    isrdict[defname] = None
    # print(isrdict.items())
    return isrdict



def simisrt(ast,isrdict):
    isrnum=len(isrdict)
    identi=c_ast.IdentifierType(['void'])
    fundetyde=c_ast.TypeDecl('simulate',[],identi)
    simdecl=c_ast.Decl('simulate',[],[],[],c_ast.FuncDecl(None,fundetyde),None,None,None)
    simu=c_ast.FuncDef(simdecl,None,c_ast.Compound([]))

    for i in range(0,isrnum):                       #isr[0] = &isr_1;
        simassiisr=astAssiIsr(i)
        simu.body.block_items.append(simassiisr)
    for isr in isrdict:                                                          #deferral[0] = &deferral_1;
        if isrdict[isr]==isr:
            simdef=astAssiDef(isr)
            simu.body.block_items.append(simdef)
    #int rand = __VERIFIER_nondet() % N;
    simveri=astVeriNon()
    simu.body.block_items.append(simveri)
    simpri=astAssiPri()
    simu.body.block_items.append(simpri)
    simfuncisr=astFuncIsr()
    simu.body.block_items.append(simfuncisr)
    simu.show()
    ast.ext.append(simu)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename  = sys.argv[1]
    else:
        filename = 'examples/c_files/year.c'

    print ("before parse_file")
    globvar=[]
    ast = parse_file(filename, use_cpp=True,
            cpp_path='gcc',
            cpp_args=['-E', r'-Iutils/fake_libc_include'])
    # ast.show()

    glbvar=[]                             #global variables
    isrdict={}
    isrdict=isrDict(ast,isrdict)
    print ("\033[1;5;32;45;1mISR Dict\033[0m")
    print(isrdict)
    print(len(isrdict))
    for ext in ast.ext:                   #store the global variables
        if typeName(ext)=='Decl':
            extname=typeName(ext.type)
            if extname=='TypeDecl':
                print( extname== 'TypeDecl')
                glbvar.append(ext.name)                         #undate list of global variables
        elif typeName(ext)=='FuncDef':
            funcname=ext.decl.name
            print("decl   "+ext.decl.name)
            if isDeferral(funcname) or isIsr(funcname):
                isrnum=funcname.split('_')[1]                       #isr is identified by name
                print(isrnum)
                # if isIsr(funcname):
                #     isrnum=isrnum+1
                for ass in ext.body.block_items:
                    assname=typeName(ass)
                    print("ass  "+assname)
                    if assname=='Assignment':
                        varl=ass.lvalue.name                  #lvalue's type of Assignment is the ID
                        varr = ass.rvalue
                        # print(varr)                  #insert reg
                        if isHalIn(varr):
                            # ext.body.show()
                            regtgtidx = ext.body.block_items.index(ass) + 1
                            ext.body.block_items.insert(regtgtidx, astScheReg(varl))
                            # ext.body.show()
                        elif varl in glbvar and not isHalOut(varr):                    #insert isr
                            # ext.body.show()
                            isrtgtidx=ext.body.block_items.index(ass)+1
                            print(isrnum)
                            astScheIsr(str(int(isrnum) - 1)).show()
                            ext.body.block_items.insert(isrtgtidx, astScheIsr(str(int(isrnum) - 1)))
                            # ext.body.show()
                    if assname=='Return' and isrdict.has_key(isrnum) and isrdict[isrnum]==isrnum:             #isr and and the corresponding deferral both exist
                        if isIsr(funcname):
                            # ext.body.show()
                            enqueidx=ext.body.block_items.index(ass)
                            ext.body.block_items.insert(enqueidx, astScheDefer(str(int(isrnum) - 1)))
                            ext.body.block_items.insert(enqueidx, astEnqueue(str(int(isrnum) - 1),'Q'))
                            # ext.body.show()
                            break
                        if isDeferral(funcname):
                            enqueidx = ext.body.block_items.index(ass)
                            ext.body.block_items.insert(enqueidx, astDequeue('Q'))
                            # ext.body.show()
                            break
    simisrt(ast,isrdict)
    # print ("\033[1;5;32;45;1mAST parsered\033[0m")
    # ast.show()
    parsered = c_generator.CGenerator()
    print ("\033[1;5;32;45;1mC parsered\033[0m")
    print(parsered.visit(ast))

    # astScheIsr(6)
    # astScheDefer(6)
    # astScheReg('r')
    # astEnqueue(1, 'R')
    # astDequeue('R')



    # print ("\033[1;5;32;45;1mast.ext[164]\033[0m")

    # print(ast.ext[167].name)
    # print(ast.ext[164].quals)
    # print(ast.ext[164].storage)
    # print(ast.ext[164].funcspec)
    # print(ast.ext[164].type)
    # print(ast.ext[164].init)
    # print(ast.ext[164].bitsize)
    # print(ast.ext[164].coord)
    # print ("\033[1;5;32;45;1mast.ext[166]\033[0m")
    # ast.ext[167].body.block_items[1].args=c_ast.Constant('int',6)
    # ast.ext[167].body.block_items[1].show()
    # print(ast.ext[167].body.block_items[1])
    # print(ast.ext[167].body.block_items[1].name)
    # print(ast.ext[167].body.block_items[1].args)
    # print(ast.ext[167].body.block_items[1].coord)
    # print(ast.ext[166].body.block_items[1].quals)
    # print(ast.ext[166].body.block_items[1].storage)
    # print(ast.ext[166].body.block_items[1].funcspec)
    # print(ast.ext[166].body.block_items[1].type)
    # print(ast.ext[166].body.block_items[1].init)
    # print(ast.ext[166].body.block_items[1].bitsize)