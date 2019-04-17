var
   i,n,k,l:integer;
   a:array of integer;
   c:array of integer;
   b:array of integer;
begin
readln(n);
k:=0;
setlength(a,n);
setlength(b,1);
setlength(c,1);
c[0]:=1;
for i:=0 to (n-1) do 
   readln(a[i]);
for i:=1 to n-1 do
   if a[i]=a[i-1] then
      begin
         b[k]:=a[i];
         c[k]:=c[k]+1;
      end
   else
   begin
      k+=1;
      setlength(b,k+1);
      setlength(c,k+1);
      b[k]:=a[i];
      c[k]:=1;
   end;
writeln('b:',c);
writeln('c:',b);
end.