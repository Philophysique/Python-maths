def PGCD(a, b):
    if b > a:
        b, a = a, b
    r = 1
    while r != 0:
        r = a%b
        a, b = b, r
    if a == 0:
        return b
    else:
        return a

def simplifier(a, b):
    if int(a/b) == a/b:
        return str(int(a/b))
    else:
        rep = str(int(a/PGCD(a,b))) + "/" + str(int(b/PGCD(a,b)))
        if "-" in rep:
            rep = rep.replace("-","")
            rep = "-" + rep
        return rep
    
def fraction(x):
    return int(x[: x.index('/')]), int(x[x.index('/') + 1:])

def correctf(f):
    f = f.replace(' ','')
    f = f.replace(')(',')*(')
    f = f.replace('**','^')
    f = f.replace('Vx','x^(1/2)')
    f = f.replace('log(x)','log(x,10)')
    f = f.replace('logx','log(x,10)')
    f = f.replace('(x)','x')
    if 'sqrt' in f:
        for i in range(len(f[f.index('sqrt')+4:])):
            if (f[f.index('sqrt') + 4:][i] == ')' and f[f.index('sqrt') + 4: f.index('sqrt') + 4 + i].count('(') == 
                f[f.index('sqrt') + 4: f.index('sqrt') + 4 + i].count(')') + 1):
                f = f.replace(f[f.index('sqrt'): f.index('sqrt') + 4 + i] + ')', f[f.index('sqrt') + 4: f.index('sqrt') + 4 + i] + ')^(1/2)')
                break
    Trigo = ['cos', 'sin', 'tan', 'sec', 'csc', 'cot', 'arcsin', 'arccos', 'arctan', 'sinh','cosh', 'tanh', 
         'sech', 'csch', 'coth', 'arcsinh', 'arccosh', 'arctanh', 'arcsech', 'arccsch', 'arccoth']
    for i in Trigo:
        if i + '(' in f:
            for j in range(len(f[f.index(i + '('):])):
                if (f[f.index(i + '('):][j] == ')' and f[f.index(i + '('): f.index(i + '(') + j + 1].count('(') == 
                    f[f.index(i + '('): f.index(i+'(') + j + 1].count(')')):
                    g = f[f.index(i+'('): f.index(i + '(') + j + 1]
                    if g + '^' in f:
                        f = f.replace(g + '^', '(' + g + ')^')
        if i + 'x^' in f:
            f = f.replace(i+'x^','('+i+'x)^')
        if i + '^' in f:
            if f[f.index(i+'^'):].index('x') > f[f.index(i+'^'):].index('('):
                for j in len(f):
                    if f[j] == 'x' and j > f.index(i + '^'):
                        k = j
                        break
                y = f[f.index(i + '^') + len(i) + 1: k]
                f = f.replace(i + '^' + y + 'x','(' + i + 'x)^' + y)
            else:
                for j in len(f):
                    if f[j] == '(' and j > f.index(i + '^'):
                        k = j
                        break
                y = f[f.index(i + '^') + len(i) + 1: k]
                for j in range(len(f[f.index(i + '^'):])):
                    if (f[f.index(i + '^'):][j] == ')' and f[f.index(i + '^'):f.index(i + '^') + j + 1].count('(') ==
                        f[f.index(i + '^'): f.index(i + '^') + j + 1].count(')')):
                        g = f[k: k + j + 1]
                        f = f.replace(i + '^' + y + g,'(' + i + g + ')^' + y)
    return f

def derivate(f):
    if '+' in f and '(' not in f:
        l = split(f)
        d = []
        for i in l:
            der = derivate(i)
            if '0*' in der or '*0' in der:
                der = ' '
            d.append(der)
        f = '(' + '+'.join(d) + ')'
        return f
    else: 
        f = correctf(f)
        if 'x' not in f:
            f = '0'
        elif f == '0':
            f = ''
            return f
        else:
            if '(' in f:
                if 'x' in f[f.index('(') + 1: f.rindex(')')] and ',' not in f:
                    if '*' in f and '/' not in f:
                        for i in range(len(f)):
                            if f[i] == '*':
                                if f[:i].count('(') == f[:i].count(')'):
                                    return product(f, i)
                        return composition(f)
                    if '/' in f and '*' not in f:
                        for i in range(len(f)):
                            if f[i] == '/':
                                if f[:i + 1].count('(') == f[:i + 1].count(')') and f.index('(') < f.index('/'):
                                    return quotient(f, i)
                                elif f[:i + 1].count('(') == 0:
                                    return inverse(f)
                        return composition(f)
                    if '/' in f and '*' in f: 
                        for i in range(len(f)):
                            if f[i] == '*':
                                if f[:i].count('(') == f[:i].count(')'):
                                    return product(f, i)
                        for i in range(len(f)):
                            if f[i] == '/':
                                if f[:i + 1].count('(') == f[:i + 1].count(')') and f.index('(') < f.index('/'):
                                    return quotient(f, i)
                                elif f[:i + 1].count('(') == 0:
                                    return inverse(f)
                            return composition(f)
                    if '/' not in f and '*' not in f: 
                        if 'x^(' in f or ')^x' in f or ')^(' in f:
                            return xpowerx(f)
                        else:
                            return composition(f)
                else:
                    if '*' in f:
                        return product(f)
                    elif ',' in f:
                        if '(x,' not in f:
                            return composition(f)
                        else:
                            return logarithm(f)
                    elif 'ln' in f:
                        return logarithm(f)
                    else:
                        return root(f)
            else:
                if '*' in f:
                    f = product(f, f.index('*'))
                    return f
                elif '/x' in f and ord(f[f.index('/x')-1]) > 47 and ord(f[f.index('/x') - 1]) < 58:
                    return f.replace('/x', '/(x^2)')
                elif '/' in f:
                    return quotient(f, f.index('/'))
                elif 'x^x' in f:
                    return xpowerx(f)
                elif '^x' in f:
                    return expo(f)
                elif 'x^' in f:
                    return power(f)
                Trigo = ['cos', 'sin', 'tan', 'sec', 'csc', 'cot', 'arcsin', 'arccos', 'arctan', 'sinh','cosh', 'tanh', 
                'sech', 'csch', 'coth', 'arcsinh', 'arccosh', 'arctanh', 'arcsech', 'arccsch', 'arccoth']
                for i in Trigo: 
                    if i in f:
                        return trig(f)
                if 'lnx' in f or 'logx' in f:
                    return logarithm(f)
                elif f == 'x':
                    return '1'
                elif f == '-x':
                    return '-1'
                else:
                    return f.replace('x', '')
    return f
    
def trig(f):
    if 'arccoth' in f:
        return f.replace('arccothx', '1/(1-x^2)')
    elif 'arccsch' in f:
        return f.replace('csch-1x', '-1/(((1/(x^2)+1)^(1/2))*x^2)')
    elif 'arcsech' in f:
        return f.replace('sech-1x', '-1/(((1/x-1)^(1/2))*((1/x+1)^(1/2))*x^2)')
    elif 'arctanh' in f:
        return f.replace('arctanhx', '1/(1-x^2)')
    elif 'arccosh' in f:
        return f.replace('arccpsh', '1/(((x-1)^(1/2))*((x+1)^(1/2)))')
    elif 'arcsinh' in f:
        return f.replace('arcsinhx', '1/((x^2+1)^(1/2))')
    elif 'coth' in f:
        return f.replace('cothx', '-(cschx)^2')
    elif 'csch' in f:
        return f.replace('cschx', '-cothx*cschx')
    elif 'sech' in f:
        return f.replace('sechx', '-tanhx*sechx')
    elif 'tanh' in f:
        return f.replace('tanhx', '(sechx)^2')
    elif 'cosh' in f:
        return f.replace('coshx', 'sinhx')
    elif 'sinh' in f:
        return f.replace('sinhx', 'coshx')
    elif 'arctan' in f:
        return f.replace('arctanx', '1/(x^2+1)')
    elif 'arccos' in f:
        return f.replace('arccosx', '-1/((1-x^2)^(1/2))')
    elif 'arcsin' in f:
        return f.replace('arcsin', '1/((1-x^2)^(1/2))')
    elif 'sin' in f:
        return f.replace('sin', 'cos')
    elif 'cos' in f:
        return '-'+f.replace('cos', 'sin')
    elif 'tan' in f:
        f = f.replace('tanx', '/((cosx)^2)')
        if f[0] == '/':
            f='1'+f
        return f
    elif 'sec' in f:
        return f.replace('secx', '(sinx)/((cosx)^2)')
    elif 'csc' in f:
        return f.replace('cscx', '(-cosx)/((sinx)^2)')
    elif 'cot' in f:
        return f.replace('cotx', '-1/((sinx)^2)')
      
def power(f):
    g = f[:f.index('x')]
    if g != '':
        if '/' not in g:
            return str(eval(f[f.index('^') + 1:] + '*' + g))+ 'x^' + str(int(f[f.index('^') + 1:]) - 1)
        else:
            return simplifier(fraction(g)[0]*eval(f[f.index('^')+1:]),fraction(g)[1]) + 'x^' + str(int(f[f.index('^') + 1:]) - 1)
    return f[f.index('^') + 1:] + 'x^' + str(int(f[f.index('^') + 1:]) -1)

def xpowerx(f):
    if 'x^x': 
        return '(' + derivate('lnx*x') + ')*' + f
    if 'x^(':
        return '(' + derivate('lnx*' + f[f.index('(') + 1: f.rindex(')')]) + ')*' + f
    elif ')^x':
        return '('+derivate('x*ln(' + f[f.index('(') + 1: f.index(')^x')] + ')') + ')*' + f
    elif ')^(':
        return '(' + derivate(f[f.index('(') + 1: f.index(')^')] + '*ln(' + f[f.index('^(') + 1: f.rindex(')')] + ')') + ')*' + f      
        
def expo(f):
    if 'e^' in f:
        return f
    return 'ln(' + f[: f.index('^')] + ')*' + f

def inverse(f):
    if '1/(' in f:
        return '-' + derivate(f[f.index('/') + 2: -1]) + '/(' + f[f.index('/') + 1:] + '^2)'
    return '-' + f[:f.index('/')] + '*' + derivate(f[f.index('/') + 2: -1]) + '/(' + f[f.index('/') + 1:] + '^2)'
 
def product(f, i):
    print(f[i:],f[:i])
    if f[i-1:i+2]==')*(':
        return '('+derivate(f[1:i-1])+')*('+f[i+2:-1]+')+('+f[1:i-1]+')*('+derivate(f[i+2:-1])+')'
    elif f[i:i+2]=='*(':
        return '('+derivate(f[:i])+')*('+f[i+2:-1]+')+('+f[:i]+')*('+derivate(f[i+2:-1])+')'
    elif f[i-1:i+1]==')*':
        return '('+derivate(f[1:i-1])+')*('+f[i+1:]+')+('+f[1:i-1]+')*('+derivate(f[i+1:])+')'
    return derivate(f[:i])+'*'+f[i+1:]+'+'+f[:i]+'*'+derivate(f[i+1:])

def quotient(f,i):
    if f[i-1:i+2]==')/(':
        return '(('+derivate(f[1:i-1])+')*('+f[i+2:-1]+')-('+f[1:i-1]+')*('+derivate(f[i+2:-1])+'))/(('+f[i+2:-1]+')^2)'
    elif f[i:i+2]=='/(':
        return '(('+derivate(f[:i])+')*('+f[i+2:-1]+')-('+f[:i]+')*('+derivate(f[i+2:-1])+'))/(('+f[i+2:-1]+')^2)'
    elif f[i-1:i+1]==')/':
        return '(('+derivate(f[1:i-1])+')*('+f[i+1:]+')-('+f[1:i-1]+')*('+derivate(f[i+1:])+'))/(('+f[i+1:]+')^2)'
    return '('+derivate(f[:i])+'*'+f[i+1:]+'-'+f[:i]+'*'+derivate(f[i+1:])+')/(('+f[i+1:]+')^2)'
 
def composition(f):
    a=f[f.index('('):f.index(')')+1]
    if ',' in f:
        g=f[f.index('(')+1:f.index(',')]
        return derivate(g)+'*'+derivate(f.replace(g,'x')).replace('x^1','x').replace('x^0','').replace('x',g)
    else:
        g=f[f.index('(')+1:f.index(')')]
    return derivate(g)+'*'+derivate(f.replace(a,'x')).replace('x^1','x').replace('x^0','').replace('x',a)

def root(f):
    if f[:f.index('x')]!='':
        if '/' not in f[:f.index('^')+1]:
            return simplifier(fraction(f[f.index('^(')+2:-1])[0]*eval(f[:f.index('x')]),fraction(f[f.index('^(')+2:-1])[1])+'x^('+str(simplifier(fraction(f[f.index('^')+2:-1])[0]-fraction(f[f.index('^')+2:-1])[1],fraction(f[f.index('^')+2:-1])[1]))+')'
        else:
            return simplifier(fraction(f[f.index('^(')+2:-1])[0]*fraction(f[:f.index('x')])[0],fraction(f[f.index('^(')+2:-1])[1]*fraction(f[:f.index('x')])[1])+'x^('+str(simplifier(fraction(f[f.index('^')+2:-1])[0]-fraction(f[f.index('^')+2:-1])[1],fraction(f[f.index('^')+2:-1])[1]))+')'
    else:
        return f[f.index('^')+2:-1]+'x^('+str(simplifier(fraction(f[f.index('^')+2:-1])[0]-fraction(f[f.index('^')+2:-1])[1],fraction(f[f.index('^')+2:-1])[1]))+')'
        
def logarithm(f):
    f=f.replace('*l','l')
    f=f.replace('lnx','ln(x)')
    if 'ln' in f:
        if f[:f.index('ln')]!='':
            if '/' not in f[:f.index('ln')]:
                return f[:f.index('ln')]+'/x'
            else:
                return str(fraction(f[:f.index('ln')])[0])+'/('+str(fraction(f[:f.index('ln')])[1])+'x)'
        else:
            return '1/x'
    else :
        if f[:f.index('log')]!='':
            if '/' not in f[:f.index('log')]:
                return f[:f.index('log')]+'/(ln('+f[f.index('log(x,')+6:-1]+')*x)'
            else:
                return str(fraction(f[:f.index('log')])[0])+'/('+str(fraction(f[:f.index('log')])[1])+'ln('+f[f.index('log(x,')+6:-1]+')*x)'
        else:
            return '1/(ln('+f[f.index('log(x,')+6:-1]+')*x)'

def correctd(d):
    d=d.replace('--','')
    d=d.replace('-+','-')
    d=d.replace('+-','-')
    d=d.replace('++','')
    d=d.replace('^1','')
    d=d.replace('x^0','')
    if 'x*1/x' in d:
        if d.index('x*1/x')==0 or d[d.index('x*1/x')-1]=='+' or d[d.index('x*1/x')-1]=='-' or d[d.index('x*1/x')-1]=='(':
            d=d.replace('x*1/x','1')
        else:
            d=d.replace('x*1/x','')
    if '1/x*x' in d:
        if d.index('1/x*x')==0 or d[d.index('1/x*x')-1]=='+' or d[d.index('1/x*x')-1]=='-' or d[d.index('1/x*x')-1]=='(':
            d=d.replace('1/x*x','1')
        else:
            d=d.replace('1/x*x','')
    if '1*' in d:
        if d.index('1*')==0:
            d=d[2:]
        d=d.replace('+1*','+')
        d=d.replace('-1*','-')
        d=d.replace('(1*','(')
        d=d.replace('*1*','*')
    if '*1' in d:
        if d.rindex('*1')==len(d)-2 :
            d=d[:-2]
        d=d.replace('*1+','+')
        d=d.replace('*1-','-')
        d=d.replace('*1)',')')
    for i in range(9):
        if chr(49+i)+'*' in d:
            if ord(d[d.index(chr(49+i)+'*')+2])<48 and ord(d[d.index(chr(49+i)+'*')+2])>57:
                d=d.replace(chr(49+i)+'*',chr(49+i))
    d=d.replace('+0','')
    if '0+' in d:
        if d.index('0+')==0 or d[d.index('0+')-1]=='+' or d[d.index('0+')-1]=='-' or d[d.index('0+')-1]=='(':
            d=d.replace('0+','')
    for i in range (10):
        d=d.replace('('+chr(48+i)+')',chr(48+i))
    return d

def split(f):
    l=f.split('+')
    j=0
    for i in range(len(l)):
        if '(' in l[j]:
            while l[j].count(')')!=l[j].count('('):
                l[j]+='+'+l[j+1]
                del l[j+1]
            if '-' in l[j][l[j].rindex(')'):]:
                    k=l[j].split('-')
                    for m in range(1,len(k)):
                        k[m]='-'+k[m]
                    l=l[:j]+k+l[j+1:]
        if j<len(l)-1:
            j+=1
    for i in l:
        if '-' in i:
            if l.index(i)!=len(l)-1:
                j=i.split('-')
                for k in range(len(j)):
                    j[k]='-'+j[k]
                l=l[:l.index(i)]+j+l[l.index(i)+1:]
            else:
                j=i.split('-')
                for k in range(len(j)):
                    j[k]='-'+j[k]
                l=l[:l.index(i)]+j
    j=0
    for i in range(len(l)):
        if '(' in l[j]:
            while l[j].count(')')!=l[j].count('('):
                l[j]+='+'+l[j+1]
                del l[j+1]
        if j<len(l)-1:
            j+=1
    for i in range(len(l)):
        l[i]=l[i].replace('+-','-')
        l[i]=l[i].replace('--','-')
    for i in l:
        if i=='-':
            del l[l.index(i)]
    return l

def nieme(d):
    j=2
    rep=input('Voulez vous calculez la dérivée seconde de votre fonction ? (o/n) ')
    while rep=='oui' or rep=='Oui' or rep=='o' or rep=='O':
        l=split(d)
        d=[]
        for i in l:
            der=derivate(i)
            if '*0' in der:
                der=''
            elif '0*' in der:
                if d.index('0*')==0 or d[d.index('0*')-1]=='+' or d[d.index('0*')-1]=='-' or d[d.index('0*')-1]=='(' or d[d.index('0*')-1]=='*':
                    der=''
            d.append(der)
        d='+'.join(d)
        d=correctd(d)
        if 'x' not in d:
            d=eval(d)
            if j==2:
                print("La dérivée seconde est constante et vaut : \nf''(x) =", d,"\ndonc la dérivée troisième est nulle.")
            else:
                print('La dérivée '+str(j)+'-ième est constante et vaut : \nf'+str(j)+'(x) =', d,'\ndonc la dérivée '+str(j+1)+'-ième est nulle.')
            break
        if j==2:
            print("La dérivée seconde de votre fonction est : \nf''(x) =", d)
        else:   
            print('La dérivée '+str(j)+'-ième de votre fonction est : \nf'+str(j)+'(x) =', d)
        j+=1
        rep=input('Voulez vous calculez la dérivée '+str(j)+'-ième de votre fonction ? (o/n) ')

def main():
    f=input('Rentrer votre fonction : ')
    arc=['arcsin','arccos','arctan','arcsinh','arccosh','arctanh','arcsech','arccsch','arccoth']
    form=['sin-1','cos-1','tan-1','sinh-1','cosh-1','tanh-1','sech-1','csch-1','coth-1']
    for i in range(len(form)):
        f=f.replace(form[i],arc[i])
    l=split(f)
    d=[]
    for i in l:
        der=derivate(i)
        if '*0' in der:
            der=''
        elif '0*' in der:
            if d.index('0*')==0 or d[d.index('0*')-1]=='+' or d[d.index('0*')-1]=='-' or d[d.index('0*')-1]=='(' or d[d.index('0*')-1]=='*':
                der=''
        d.append(der)
    d='+'.join(d)   
    d=correctd(d)
    if 'x' not in d:
        d=eval(d)
        print("La dérivée première de f est constante et vaut : \nf'(x) =", d,"\ndonc la dérivée seconde est nulle.")
    else:
        print("La dérivée première de votre fonction est : \nf'(x) =", d)
        #nieme(d)

main()  