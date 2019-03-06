var s,n,k,i,j,h,w,x1,x2,y2,y1:integer;
   a:array [0..100, 0..100] of integer;
begin
readln(w,h);
readln(n);
s:=0;
for i:=0 to 100 do
   for j:=0 to 100 do
      a[i][j]:=0;
for k:=1 to n do
   begin
   readln(x1,y1,x2,y2);
   for i:=x1 to x2 do
      for j:=y1 to y2 do
      a[i][j]:=1;
   end;
for i:=0 to 100 do
   for j:=0 to 100 do
      s+=a[i][j];
writeln(w*h-s)
end.