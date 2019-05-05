type
    ar=array of real;

var
    i,n:integer;
    a:ar;

procedure Smooth2(mas:ar;n:integer);
    var
        sum:real;
        i:integer;
    begin
        sum:=mas[0];
        for i:=1 to n-1 do
            begin
                sum+=mas[i];
                mas[i]:=sum/2;
                sum-=mas[i-1];
            end;

    end;

begin
readln(n);
setlength(a,n);
for i:=0 to n-1 do
    readln(a[i]);
for i:=1 to 5 do
    Smooth2(a,n);
writeln(a);
end.