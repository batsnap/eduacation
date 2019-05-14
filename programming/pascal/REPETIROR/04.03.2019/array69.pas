var
n,i:integer;
a,x:real;
m:array of real;
begin
readln(n);
SetLength(m,n);
for i:=1 to n do
   begin
   readln(a);
   m[i]:=a;
   end;
i:=1;
while i<=Length(m) do
begin
   x:=m[i];
   m[i]:=m[i+1];
   m[i+1]:=x;
   i:=i+2
end;
for i:=1 to n do
begin
   write(m[i]:0:0);  
   write(' ');
end;
end.