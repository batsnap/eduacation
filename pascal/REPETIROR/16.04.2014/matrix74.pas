var
   i,k,m,n,j:integer;
   a:array of array of integer;
begin
k:=1;
readln(m);
readln(n);
setlength(a,m);
for i:=0 to m-1 do
   begin
      setlength(a[i],n);
      for j:=0 to n-1 do
         a[i][j]:=10*k;
      k+=1;
      writeln(a[i]);
   end;

end.