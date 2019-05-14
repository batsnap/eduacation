type
    mat=array of array of real;
    ar=array of real;
var
    i,k,n,m:integer;
    a:ar;
    b:mat;
procedure ArrayToMatrRow(a:ar;b:mat;n,m,k:integer);
    var
        i,x,y:integer;
    begin
        x:=0;
        y:=0;
        for i:=0 to k-1 do
            if (y<m) then
                begin
                    b[x,y]:=a[i];
                    y+=1;
                end 
            else
                begin
                    y:=0;
                    x+=1;
                    b[x,y]:=a[i];
                    y+=1;
                end;

    end;

begin
    readln(k);
    readln(n,m);
    setlength(a,k);
    setlength(b,n);
    for i:=0 to n-1 do 
        setlength(b[i],m);
    for i:=0 to k-1 do
        readln(a[i]);
    ArrayToMatrRow(a,b,n,m,k);
    for i:=0 to n-1 do
        writeln(b[i]);
end.
