type
    ar=array of real;

var
    i,n:integer;
    a:ar;

procedure Smooth3(mas:ar;n:integer);
    var
        sum,x:real;
        i:integer;
        buf:ar;
    begin
        buf:=mas; 
        for i:=0 to n-1 do
            begin
                if i=0 then
                    buf[i]:=mas[i+1];
                if (i>0) and (i<>n-1) then
                    buf[i]:=(mas[i-1]+mas[i+1])/2;
                if i=n-1 then
                    buf[i]:=mas[i-1];
                a:=buf;
            end;
    end;

begin
readln(n);
setlength(a,n);
for i:=0 to n-1 do
    readln(a[i]);
for i:=1 to 5 do
    begin
        Smooth3(a,n);
        writeln(a);
    end;
end.