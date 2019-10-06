import os

counter = 0
b = True
while b == True:
    print ('Enter the x coordinate of the triangle vertex:')
    #vertex
    xa = float(input())
    a = str(xa)
    if (len(a) == 6 and a[3] == '.' and a[0] != '-') or (len(a) == 7 and a[4] == '.' and a[0] == '-'):
        print ('Enter the x coordinate of the triangle base:')
        #base
        xb = float(input())
        a = str(xb)
        if (len(a) == 6 and a[3] == '.' and a[0] != '-') or (len(a) == 7 and a[4] == '.' and a[0] == '-'):
            print ('Enter the length of the base:')
            #length of the base
            bc = float(input())
            a = str(bc)
            if len(a) == 6 and a[3] == '.' and a[0] != '-':        
                print ('Enter the x coordinate of the center of the circle:')
                #the center of the circle
                xo = float(input())
                a = str(xo)
                if (len(a) == 6 and a[3] == '.' and a[0] != '-') or (len(a) == 7 and a[4] == '.' and a[0] == '-'):
                    print ('Enter the radius of the circle:')
                    #radius
                    r = float(input())
                    a = str(r)
                    if len(a) != 6 or a[3] != '.' or a[0] == '-':
                        print ('invalid data format, try again:')
                    else:
                        b = False
                else:
                    print ('invalid data format, try again:')
            else:
                print ('invalid data format, try again:')
        else:
            print ('invalid data format, try again:')
    else:
        print ('invalid data format, try again:')
        
    while b == False:
        #___1
        if xb == (r+xo) and xa<xb:
            print ('regard')
            counter +=1
            
        #___2
        if xa == (r+xo) and xa<xb:
            print ('regard')
            counter +=1
            
        #___3
        if xa == (xo-r) and xa>xb:
            print ('regard')
            counter +=1
            
        #___4
        if xb == (xo-r) and xa<xb:
            print ('regard')
            counter +=1
            
        #___5,10 vertex in circle
        if xa<(xo+r) and xa>(xo-r):
            # the base outside the circle
            if xb >= (xo+r) or xb <= (xo-r):
                print('cross')
                counter +=1
            # the base in the circle
            else:
                if ((bc/2) == (r**2-(xb-xo)**2)**0.5 and xa<xb) or ((bc/2) == (r**2-(xo-xb)**2)**0.5 and xa>xb):
                    print('regard')
                    counter +=1
                    if abs(xo) == abs((xa-xb)/2):
                        print('concentricity')
                    else:
                        print('non-concentricity')
                if ((bc/2) > (r**2-(xb-xo)**2)**0.5 and xa<xb) or ((bc/2) > (r**2-(xo-xb)**2)**0.5 and xa>xb):
                    print('cross')
                    counter +=1
                if ((bc/2) < (r**2-(xb-xo)**2)**0.5 and xa<xb) or ((bc/2) < (r**2-(xo-xb)**2)**0.5 and xa>xb):
                    print('no points in common')
                    
        #___6 the vertex outside the circle and:
        if xa > (xo+r) or xa < (xo-r):
            #base in the circle
            if xb > (xo-r) and xb < (xo+r):
                print('cross')
                counter +=1
            #the base outside the circle
            if xb < (xo-r) or xb> (xo+r):
                x = (xo**2-xa*xo-r**2)/(xo-xa)
                y = (r**2-(x-xo)**2)**0.5
                y1 = y/(x-xa)*xb-xa
                
                if y1 == (bc/2):
                    print('regard')
                    counter +=1
                    if xo == (xb+(xa-xb)/4):
                        print('concentricity')
                    else:
                        print('non-concentricity')
        if counter == 0:
            print('no points in common')
        b = True
        print('Enter any key to continue:')
        c = input()
        os.system('cls')