var
   i,k,m,n,j:integer;
   a,b:array of array of real;
begin
randomize;
k:=1;
readln(m);
readln(n);
setlength(a,m+2);
setlength(b,m);
for i:=0 to m+1 do
   begin
      setlength(a[i],n+2);
      for j:=0 to n+1 do
         a[i][j]:=100;
   end;

for i:=1 to m do
   begin
      setlength(b[i-1],n);
      for j:=1 to n do
         a[i][j]:=random(-100,100);
      end;
for i:=0 to m+1 do
   writeln(a[i]);
writeln('--------------------------------------');
for i:=1 to m do
   begin
      for j:=1 to n do
         if (a[i][j]<a[i-1][j]) and (a[i][j]<a[i+1][j]) and (a[i][j]<a[i][j-1]) and (a[i][j]<a[i][j+1]) and (a[i][j]<a[i+1][j+1]) and (a[i][j]<a[i-1][j-1]) and (a[i][j]<a[i-1][j+1]) and (a[i][j]<a[i+1][j-1]) then
            b[i-1][j-1]:=0
         else
            b[i-1][j-1]:=a[i][j];
   end;
for i:=0 to m-1 do
   writeln(b[i]);
end.