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
for i:=2 to (n-1) do 
   begin
      m[i]:=(m[i-1]+m[i+1])/2;
   end;
for i:=1 to n do
begin
   write(m[i]:0:0);  
   write(' ');
end;
end.