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

end.