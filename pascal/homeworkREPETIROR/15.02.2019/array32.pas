var n,i,s:integer;
    c:real;
    a: array of real;
begin
s:=0;
read(n);
SetLength(a,n);
for i:=1 to n do
begin
    read(c);
    a[i]:=c;
    end;
i:=2;
while not ((i+1<=n) or ((a[i-1]>a[i])and(a[i+1]>a[i]))) do
    i+=1;
if (i+1=n) then
    write('nety')
else
    write(i);
end.