var n,i,c,k:integer;
    a: array of integer;
begin
read(n);
k:=0;
SetLength(a,n);
for i:=1 to n do
begin
    read(c);
    a[i]:=c;
end;
k:=a[n] div a[n-1];
n:=n-2;
while ((n>=2)and(a[n] div a[n-1]=k)) do n:=n-1;
if (n=1) then 
    write(k)
else
    write(0)
end.