type p= record
x:integer;
y:integer;
end;

function pr(x1,x2,y2,y1:integer):real;
begin
pr:= sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
end;

var a:array of p;
i,n,j,k,c:integer;
per:real;
begin
readln(n);
per:=0;
setlength(a,n);
for i:= 0 to n-1 do
   with a[i] do begin 
      read(x,y);
        end;
for i:=0 to n-1 do 
    for j:=1  to n-1 do 
    for k:=2 to n-1 do 
        if (per<(pr(a[i].x,a[j].x,a[i].y,a[j].y)+pr(a[k].x,a[j].x,a[k].y,a[j].y)+pr(a[i].x,a[k].x,a[i].y,a[k].y))) then
            per:=pr(a[i].x,a[j].x,a[i].y,a[j].y)+pr(a[k].x,a[j].x,a[k].y,a[j].y)+pr(a[i].x,a[k].x,a[i].y,a[k].y);
writeln(per);
end.