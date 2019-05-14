var
   i,j,n,m,max,maxid:integer;
   a:array of array of integer;
   c,b:array of integer;
begin
randomize;
readln(m,n);
setlength(a,m);
setlength(c,m);
setlength(b,m);
for i:=0 to m-1 do
   begin
      setlength(a[i],n);
      for j:=0 to n-1 do
         a[i][j]:=random(0,100);
      writeln(a[i]);
   end;
for i:=0 to m-1 do
   c[i]:=a[i][0];
max:=c[0];
maxid:=0;
writeln('------------------');
for i:=0 to m-1 do
   begin
   for j:=0 to m-1 do
      begin
         if c[j]>max then
            begin
               max:=c[j];
               maxid:=j;
            end;
      end;
   c[maxid]:=-1;
   b[i]:=maxid;
   max:=c[0];
   maxid:=0;
   end;
writeln(b);
writeln(length(b));
writeln('------------------');

for i:=m-1 downto 0 do
   writeln(a[b[i]]);
end.