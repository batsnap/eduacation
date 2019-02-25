var n,i,c:integer;
    a: array of integer;
begin
read(n);
SetLength(a,n);
for i:=1 to n do
begin
    read(c);
    a[i]:=c;
    end;
i:=1;
while (((abs(a[i] mod 2)=0) and (abs(a[i+1] mod 2)=1))or((abs(a[i] mod 2)=1) and (abs(a[i+1] mod 2)=0)))and (i<>n) do
    i+=1;
if i=n then 
    write(0)
else
    write(i+1)
end.