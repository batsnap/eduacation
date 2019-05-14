var
n,i,k,l,j:integer;
a,x:real;
m:array of real;
begin
readln(n);
readln(k,l);
SetLength(m,n);
j:=0;
for i:=1 to n do
   begin
   readln(a);
   m[i]:=a;
   end;
for i:=k+1 to (l-2) do
   begin
      x:=m[i];
      m[i]:=m[l-j];
      m[l-j]:=x;
      j:=j+1;
   end;
for i:=1 to n do
begin
   write(m[i]:0:0);  
   write(' ');
end;
end.