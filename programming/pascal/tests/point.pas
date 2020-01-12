type xy=record
    x:integer;
    y:integer;
    len:real;
end;
var
    point:array of xy;
    z,n,i,j:integer;
    k:real;
begin
    write('введите кол-во точек: ');
    read(n);
    setlength(point,n);
    for i:=0 to (n-1) do
        with point[i] do
            begin
                readln(x,y);
                len:=sqrt(x*x+y*y);
            end;        
    writeln('------------');
    for i:=0 to (n-1) do
        with point[i] do
            writeln(x,' ',y,' ',len);        
    for i:=0 to (n-2) do
        for j:=0 to (n-2-i) do
            begin
                if (point[j].len>point[j+1].len) then
                begin
                    k := point[j].len;
                    point[j].len:=point[j+1].len;
                    point[j+1].len := k;
                    z:=point[j].x;
                    point[j].x:=point[j+1].x;
                    point[j+1].x:=z;
                    z:=point[j].y;
                    point[j].y:=point[j+1].y;
                    point[j+1].y:=z;
                end;
            end;
    writeln('------------');
    for i:=0 to (n-1) do
        with point[i] do
            writeln(x,' ',y,' ',len);
end.