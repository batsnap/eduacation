var
   smax,x1max,y1max,x2max,y2max,x3max,y3max,pmax:real;
   i,j,k,n:integer;
   y:array of real;
   x:array of real;
function dlina(x1,y1,x2,y2:real):real;
begin
   dlina:=sqrt(sqr(x1-x2)+sqr(y1-y2));
end;
function perimetr(x1,y1,x2,y2,x3,y3:real):real;
begin
   perimetr:=(dlina(x1,y1,x2,y2)+dlina(x1,y1,x3,y3)+dlina(x3,y3,x2,y2));
end;
begin
pmax:=0;
readln(n);
setlength(x,n);
setlength(y,n);
for i:=0 to n-1 do
   readln(x[i],y[i]);
for i:=0 to n do
   for j:=i+1 to n-1 do
      for k:=j+1 to n-1 do
         if pmax<perimetr(x[i],y[i],x[j],y[j],x[k],y[k]) then
            begin
            pmax:=perimetr(x[i],y[i],x[j],y[j],x[k],y[k]);
            x1max:=x[i];
            y1max:=y[i];
            x2max:=x[j];
            y2max:=y[j];
            x3max:=x[k];
            y3max:=y[k];
            end;
writeln(pmax);
writeln(x1max,' ',y1max);
writeln(x2max,' ',y2max);
writeln(x3max,' ',y3max);


end.