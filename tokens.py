tokendict = {
"+"    : "PLUS"
,"++"  : "PLUSPLUS" #testing purposes
,"-"   : "MINUS"
,"*"   : "TIMES"
,"/"   : "DIVIDE"
,"("   : "LPAREN"
,")"   : "RPAREN"
        }

parsedict = dict([token[::-1] for token in tokendict.iteritems()]) #So we can recombine

#for error walkers

ops = [tokendict["+"], tokendict["-"], tokendict["*"]]
