type
    mat=array of array of real;
    ar=array of real;
var
    i,n,m,j:integer;
    a:mat;

function max1(a:ar):real;
    var
        i:integer;
        x:real;
    begin
        x:=a[0];
        for i:=0 to length(a)-1 do
            if a[i]>x then
                x:=a[i];
        max1:=x;
    end;

function Norm1(a:mat;n,m:integer):real;
    var
        k:ar;
        i:integer;
    begin
        setlength(k,m);
        for i:=0 to n-1 do
            k[i]:=max1(a[i]);
        Norm1:=max1(k);
    end;

begin
    readln(n,m);
    setlength(a,n);
    for i:=0 to n-1 do
        begin
            setlength(a[i],m);
            for j:=0 to m-1 do
                readln(a[i,j]);
        end;
writeln('ответ:',Norm1(a,n,m));
end.