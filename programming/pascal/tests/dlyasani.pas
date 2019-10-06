uses SysUtils;
var 
xa,xb,bc,xo,r,x,y,y1:real;
a:string;
i,counter:integer;
b:boolean;

begin
    counter:=0;
    b:=true;
    while (b=true) do
        begin
            writeln('Enter the x coordinate of the triangle vertex');
            readln(a);
            xa:=StrToFloat(a);
            if  ((length(a)=6) and (a[4]='.') and (a[1]<>'-')) or ((length(a) = 7) and (a[5] = '.') and (a[1] = '-')) then
                begin
                    writeln('Enter the x coordinate of the triangle base');
                    readln(a);
                    xb:=StrToFloat(a);
                    if  ((length(a)=6) and (a[4]='.') and (a[1]<>'-')) or ((length(a) = 7) and (a[5] = '.') and (a[1] = '-')) then
                        begin
                            writeln('Enter the length of the base:');
                            readln(a);
                            bc:=StrToFloat(a);
                            if  (length(a)=6) and (a[4]='.') and (a[1]<>'-') then
                                begin
                                    writeln('Enter the x coordinate of the center of the circle:');
                                    readln(a);
                                    xo:=StrToFloat(a);
                                    if  ((length(a)=6) and (a[4]='.') and (a[1]<>'-')) or ((length(a) = 7) and (a[5] = '.') and (a[1] = '-')) then
                                        begin
                                            writeln('Enter the radius of the circle:');
                                            readln(a);
                                            r:=StrToFloat(a);
                                            if (length(a)=6) and (a[4]='.') and (a[1]<>'-') then
                                                b:=false
                                            else
                                                begin
                                                    writeln('invalid data format, try again:')
                                                end
                                        end
                                    else
                                        writeln('invalid data format, try again:');
                                end
                            else
                                writeln('invalid data format, try again:');
                        end
                    else
                        writeln('invalid data format, try again:');
                end
            else
                writeln('invalid data format, try again:');
            while b=false do
                begin
                    //___1
                    if (xb=(r+xo)) and (xa<xb) then
                        begin
                            writeln('regard');
                            counter+=1;
                        end;
                    //___2
                    if ((xa=(r+xo)) and(xa<xb)) then
                        begin
                            writeln('regard');
                            counter+=1;
                        end;
                    //___3
                    if ((xa=(xo-r)) and (xa>xb)) then
                        begin
                            writeln('regard');
                            counter+=1;
                        end;
                    //___4
                    if ((xb=(xo-r)) and (xa<xb)) then
                        begin
                            writeln('regard');
                            counter+=1;
                        end;
                    //___5,10 vertex in circle
                    if ((xa<(xo+r)) and (xa>(xo-r))) then
                        //the base outside the circle
                        if ((xb>=(xo+r)) or (xb<=(xo-r))) then
                            begin
                                writeln('cross');
                                counter+=1
                            end
                        else
                            begin
                                if (((bc/2)=(sqrt(r*r-(xb-xo)*(xb-xo)))) and (xa<xb)) or ((((bc/2)=(sqrt(r*r-(xo-xb)*(xo-xb)))) and (xa>xb))) then
                                    begin
                                        writeln('reagard');
                                        counter+=1;
                                        if (abs(xo))=(abs((xa-xb)/2)) then
                                            writeln('concentricity')
                                        else
                                            writeln('non-concentricity');
                                    end;
                                if (((bc/2)=(sqrt(r*r-(xb-xo)*(xb-xo)))) and (xa<xb)) or ((((bc/2)>(sqrt(r*r-(xo-xb)*(xo-xb)))) and (xa>xb))) then
                                    begin
                                        writeln('cross');
                                        counter+=1;
                                    end;
                                if (((bc/2)=(sqrt(r*r-(xb-xo)*(xb-xo)))) and (xa<xb)) or ((((bc/2)<(sqrt(r*r-(xo-xb)*(xo-xb)))) and (xa>xb))) then
                                    writeln('no points in common');
                            end;
                    //___6 the vertex outside the circle and:
                    if (xa>(xo+r)) or (xa<(xo-r)) then
                        //base in the circle
                        begin
                            if (xb>(xo-r))and(xb>(xo+r)) then
                                begin
                                    writeln('cross');
                                    counter+=1
                                end;
                        //the base outside the circle
                        if (xb<(xo-r))or(xb<(xo+r)) then
                            begin
                                x:=(xo*xo-xa*xo-r*r)/(xo-xa);
                                y:=sqrt(r*r-(x-xo)*(x-xo));
                                y1:=y/((x-xa)*xb)-xa;
                                if y1=bc/2 then
                                    begin
                                        writeln('regard');
                                        counter+=1;
                                        if xo=(xb+((xa-xb)/4)) then
                                            writeln('concentricity')
                                        else
                                            writeln('non-concentricity');
                                    end;
                            end;
                        end;
                    if counter=0 then
                        writeln('no points in common');
                    b:=true;
                    writeln('enter any key to continue');
                    readln();
                end;
        end;
end.