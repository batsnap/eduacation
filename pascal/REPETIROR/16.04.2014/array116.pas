var
   i,n,k,l:integer;
   a:array  of integer;
   c:array [1..10] of integer;
   b:array [1..10] of integer;
begin
k:=1;
l:=2;
readln(n);
setlength(a,n);
for i:=0 to n-1 do
   readln(a[i]);
for i:=1 to (n-2) do
   if a[i]=a[i-1] then
      begin
         
         c[k]:=a[i-1];
         b[k]:=l;
         l+=1;
      end
   else
      begin
         k+=1;
         l:=1;
         c[k]:=a[i+1];
         b[i]:=l;
      end;
writeln('b:',b);
writeln('c:',c);

end.