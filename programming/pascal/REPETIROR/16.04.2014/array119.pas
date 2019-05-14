var
   n,i,j,k,l,c,r,dl:integer;
   b,a:array of integer;
begin
readln(n);
setlength(a,n);
c:=n;
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
writeln('l:',l);{это для проверки}
for k:=0 to l-2 do
   begin
   r:=a[b[k]];
   dl:=length(a)+1;
   writeln('a:',a);{это для проверки}
   writeln('a:[0,1,2,3,4,5,6,7,8,9,10,11,12]');{это для проверки}
   writeln('b:',b);{это для проверки}
   writeln('c:',c);{это для проверки}
   while length(a)<>dl do
         begin
            inc(c);
            setlength(a,c);
            for j:=c-2 downto b[k+1] do
               a[j+1]:=a[j];
         end;
      for i:=b[k] to (b[k+1]) do
         a[i]:=r;
      for j:=0 to l-1 do
         b[j]+=1;
   end;
setlength(a,c+1);
a[c]:=a[c-1];
writeln('a:',a);
end.