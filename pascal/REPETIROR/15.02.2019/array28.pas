var n,i:integer;
    c,min:real;
    a: array of real;
begin
read(n);
SetLength(a,n);
for i:=1 to n do
begin
    read(c);
    a[i]:=c;
    end;
min:=a[2];
i:=4;
while i<=n do
    if a[i]<min then
    begin
    min:=a[i];
    i+=2;
    end
    else
    i+=2;
write(min:1:1);
end.