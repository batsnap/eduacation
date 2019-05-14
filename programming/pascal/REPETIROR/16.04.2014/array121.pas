var
   n,i,j,k,l,c,r:integer;
   b,a:array of integer;
begin
readln(n);
readln(k);
setlength(a,n);
c:=n;
l:=1;
setlength(b,l+1);
for i:=0 to n-1 do  
      readln(a[i]);
for i:=1 to n-1 do  
   if a[i]<>a[i-1] then
      begin
         inc(l);
         setlength(b,l);
         b[l-1]:=i;
      end;
if k>length(b) then
   writeln(a)
else
   begin
      r:=a[b[k-1]];
      while length(a)<>n+(b[k]-b[k-1]) do
      begin
         inc(c);
         setlength(a,c);
            for j:=c-2 downto b[k] do
               a[j+1]:=a[j];
      end;
   for i:=b[k] to (b[k]+(b[k]-b[k-1])-1) do
      a[i]:=r;
   end;
writeln('a:',a);
writeln('l:',l);
writeln('b:',b);
end.