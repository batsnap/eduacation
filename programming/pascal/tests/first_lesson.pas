type xy=record
    x:integer;
    y:integer;
end;
var
    a:array of xy;
    n,i:integer;
    xmax,ymax:integer;
    len:real;
begin
    len:=0;
    write('введите кол-во точек:');
    read(n);
    setlength(a,n);
    for i:=1 to n do
        with a[i] do
            begin
                readln(x,y);
                if (sqrt(x*x+y*y)>len) then
                    begin
                        xmax:=x;
                        ymax:=y;
                        len:=sqrt(x*x+y*y);
                    end;
            end;        
    writeln('точка:',xmax,' ',ymax);
end.