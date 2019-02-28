var
   a:real;
   c: array of array of integer;
   n,i,j,k: integer;
begin
read(n);
randomize;
SetLength(c,n);
for i:=0 to (n-1) do
   SetLength(c[i],n);
for i:=0 to (n-1) do
   for j:=0 to (n-1) do
      begin
         c[i][j]:=random(100);
      end;
for i:=0 to (n-1) do
   begin
      for j:=0 to (n-1) do
         write(c[i][j],' ');
      writeln();
   end;
k:=1;
for i:=0 to (n-1) do
   begin
   for j:=0 to (n-1-k) do
      c[i][j]:=0;
   k+=1;
   end;
writeln();
for i:=0 to (n-1) do
   begin
      for j:=0 to (n-1) do
         write(c[i][j],' ');
      writeln();
   end;
end.