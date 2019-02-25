var x,e:real;
function exp1(x,e:real):real;
var sum,fac,l,k:real;
    i:integer;
begin
    
    fac:=1;
    l:=1*x;
    k:=l/fac;
    sum:=k+1;
    i:=2;
    while k>e do
    begin
    fac:=fac*i;
    l:=l*x;
    k:=l/fac;
    sum:=sum+k;
    i+=1;
    end;
    exp1:=sum-k;
end;
begin
read(x,e);
writeln(exp1(x,e):0:7);
end.
