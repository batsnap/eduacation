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
for i:=1 to n-1 do
    if a[i]>a[i+1] then
    begin
    s+=1;
    write(i,' ');
    end;
writeln(s);
end.