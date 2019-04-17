var
   a:array of integer;
   i,j,n,k:integer;
begin
readln(n);
setlength(a,n);
k:=n;
for i:=0 to n-1 do  
   readln(a[i]);
for i:=n-2 downto 0 do
   begin
   writeln(a);
   if a[i+1]<>a[i] then
      begin
         inc(k);
         setlength(a,k);
         for j:=k-2 downto i do
            a[j+1]:=a[j];
         a[i+1]:=0;
      end;
   end;
setlength(a,k+1);
writeln(a);
end.