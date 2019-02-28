var
n,i,min,max:integer;
a,x,min1,max1:real;
m:array of real;
begin
readln(n);
SetLength(m,n);
for i:=1 to n do
   begin
   readln(a);
   m[i]:=a;
   end;
max:=1;
min:=1;
min1:=m[1];
max1:=m[1];
for i:=1 to n do
begin
   if m[i]>max1 then
      begin
         max1:=m[i];
         max:=i;
      end;
   if m[i]<min1 then
   begin
      min1:=m[i];
      min:=i;
   end;
end;
for i:=min+1 to (max-1) do
   m[i]:=0;
for i:=1 to n do
begin
   write(m[i]:0:0);  
   write(' ');
end;
end.
end.