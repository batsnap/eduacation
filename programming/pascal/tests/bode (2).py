r = -1000
while True:
    print ('Enter the x coordinate of the triangle vertex:')
    #vertex
    xa = float(input())
    if xa<=999.99 and xa>=-999.99:
        xa = str(xa)
        if xa[-2] == '.' or xa[-3] == '.':
            xa = float(xa)
            print ('Enter the x coordinate of the triangle base:')
            #base
            xb = float(input())
            while xa == xb:
                print ('invalid data format, try again:')
                print ('Enter the x coordinate of the triangle base:')
                xb = float(input())                
            if xb<=999.99 and xb>=-999.99:
                xb = str(xb)
                if xb[-2] == '.' or xb[-3] == '.':
                    xb = float(xb)
                    print ('Enter the length of the base:')
                    #length of the base
                    bc = float(input())
                    if bc<=999.99 and bc>=-999.99:
                        bc = str(bc)
                        if bc[-2] == '.' or bc[-3] == '.':
                            bc = float(bc)
                            print ('Enter the x coordinate of the center of the circle:')
                            #the center of the circle
                            xo = float(input())
                            if xo<=999.99 and xo>=-999.99:
                                xo = str(xo)
                                if xo[-2] == '.' or xo[-3] == '.':
                                    xo = float(xo)
                                    print ('Enter the radius of the circle:')
                                    #radius
                                    r = float(input())
                                    if r<=999.99 and r>=-999.99:
                                        r = str(r)
                                        if r[-2] != '.' and r[-3] != '.':
                                            print ('invalid data format, try again:')
                                        else:
                                            r = float(r)
                                    else:
                                        print ('invalid data format, try again:')                                            
                                else:
                                    print ('invalid data format, try again:')
                            else:
                                print ('invalid data format, try again:')
                        else:
                            print ('invalid data format, try again:')                                            
                    else:
                        print ('invalid data format, try again:')                                            
                else:
                    print ('invalid data format, try again:')
            else:
                print ('invalid data format, try again:')
        else:
            print ('invalid data format, try again:')
    else:
        print ('invalid data format, try again:')
    
    while r != -1000:
        #___1
        if xb == (r+xo) and xa<xb:
            print ('regard')
            print('Enter any key to continue:')
            r = input()
            break
            
        #___2
        if xa == (r+xo) and xa<xb:
            print ('regard')
            print('Enter any key to continue:')
            r = input()
            break 
            
        #___3
        if xa == (xo-r) and xa>xb:
            print ('regard')
            print('Enter any key to continue:')
            r = input()
            break 
            
        #___4
        if xb == (xo-r) and xa<xb:
            print ('regard')
            print('Enter any key to continue:')
            r = input()
            break 
            
        #___5,10 vertex in circle
        if xa<(xo+r) and xa>(xo-r):
            # the base outside the circle
            if xb >= (xo+r) or xb <= (xo-r):
                print('cross')
                print('Enter any key to continue:')
                r = input()
                break 
            # the base in the circle
            else:
                if ((bc/2) == (r**2-(xb-xo)**2)**0.5 and xa<xb) or ((bc/2) == (r**2-(xo-xb)**2)**0.5 and xa>xb):
                    print('regard')
                    if abs(xo) == abs((xa-xb)/2):
                        print('concentricity')
                        print('Enter any key to continue:')
                        r = input()
                        break                         
                    else:
                        print('non-concentricity')
                        print('Enter any key to continue:')
                        r = input()
                        break                        
                if ((bc/2) > (r**2-(xb-xo)**2)**0.5 and xa<xb) or ((bc/2) > (r**2-(xo-xb)**2)**0.5 and xa>xb):
                    print('cross')
                    print('Enter any key to continue:')
                    r = input()
                    break 
                if ((bc/2) < (r**2-(xb-xo)**2)**0.5 and xa<xb) or ((bc/2) < (r**2-(xo-xb)**2)**0.5 and xa>xb):
                    print('no points in common')
                    print('Enter any key to continue:')
                    r = input()
                    break                     
                    
        #___6 the vertex outside the circle and:
        if xa > (xo+r) or xa < (xo-r):
            #base in the circle
            if xb > (xo-r) and xb < (xo+r):
                print('cross')
                print('Enter any key to continue:')
                r = input()
                break                 
            #the base outside the circle
            if xb < (xo-r) or xb> (xo+r):
                x = (xo**2-xa*xo-r**2)/(xo-xa)
                y = (r**2-(x-xo)**2)**0.5
                y1 = y/(x-xa)*xb-xa
                
                if (((r**2-(x-xo)**2)**0.5)/(((xo**2-xa*xo-r**2)/(xo-xa))-xa)*xb-xa) == (bc/2):
                    print('regard')
                    if xo == (xb+(xa-xb)/4):
                        print('concentricity')
                        print('Enter any key to continue:')
                        r = input()
                        break                         
                    else:
                        print('non-concentricity')
                        print('Enter any key to continue:')
                        r = input()
                        break                         
                
                if (((r**2-(x-xo)**2)**0.5)/(((xo**2-xa*xo-r**2)/(xo-xa))-xa)*xb-xa) > (bc/2):
                    print('no points in common')
                    print('Enter any key to continue:')
                    r = input()
                    break                     
                if (((r**2-(x-xo)**2)**0.5)/(((xo**2-xa*xo-r**2)/(xo-xa))-xa)*xb-xa) < (bc/2):
                    print('cross')
                    print('Enter any key to continue:')
                    r = input()
                    break
        print('no points in common')
        print('Enter any key to continue:')
        r = input()
        break