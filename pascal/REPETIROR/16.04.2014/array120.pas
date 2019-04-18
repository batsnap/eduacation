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
writeln('b:',b);{это для проверки}
for k:=0 to l-1 do
   begin
      writeln('a:',a);{это для проверки}
      writeln('b:',b);{это для проверки}
      c-=1;
      for j:=b[k] to c-1 do
         a[j]:=a[j+1];
      for j:=0 to l-1 do
         b[j]+=1;
      setlength(a,c)
   end;
writeln('a:',a);
end.