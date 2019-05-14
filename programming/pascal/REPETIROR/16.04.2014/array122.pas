var
   n,i,j,k,l,r,f:integer;
   b,a,c:array of integer;
begin
readln(n);
readln(k);
setlength(a,n);
l:=1;
setlength(b,l+1);
for i:=0 to n-1 do  
      read(a[i]);
for i:=1 to n-1 do  
   if a[i]<>a[i-1] then
      begin
         inc(l);
         setlength(b,l);
         b[l-1]:=i;
      end;
writeln('b:',b);
if k>length(b) then
   writeln(a)
else if k=l then 
   begin
      setlength(c,(b[k-1]));
      for i:=0 to b[k-1]-1 do
         c[i]:=a[i];
         writeln('a:',c);
   end
else
   begin
      setlength(c,n-(b[k]-b[k-1]));
      for i:=0 to b[k-1] do
         c[i]:=a[i];
      for i:=b[k] to n-1 do
         c[i-b[k]+b[k-1]]:=a[i];
         writeln('a:',c);
   end;
end.