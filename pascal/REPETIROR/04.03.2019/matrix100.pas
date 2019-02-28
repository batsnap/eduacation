var
   a:real;
   c: array of array of integer;
   n,i,j,k: integer;
procedure change(x,y,z,w:integer);
   var a,b,c,d:integer;
   begin
   a:=x;
   b:=y;
   c:=z;
   d:=w;
   y:=a;
   z:=b;
   w:=c;
   x:=d;
   end;
   

begin
readln(n,i,j,k);
change(n,i,j,k);
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
k:=0;
for i:=0 to n-1 do
   begin
      k:=0;
      for j:=i to (n-i-1) do
            begin
               writeln(c[j][j+k],c[j+k][n-1],c[n-1][n-1-k],c[n-k-1][j]);
               change(c[j][j+k],c[j+k][n-1],c[n][n-1-k],c[n-1-k][j]);
               k+=1;
            end;
   end;
for i:=0 to (n-1) do
   begin
      for j:=0 to (n-1) do
         write(c[i][j],' ');
      writeln();
   end;
end.
