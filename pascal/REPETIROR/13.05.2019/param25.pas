type
    ar=array of array of real;

var
    mat:ar;
    j,i,m:integer;
procedure outmat(var a:ar;m:integer);
    var
        i,j:integer;
    begin
        for i:=0 to m-1 do
        begin
            for j:=0 to m-1 do
                write(mat[i,j]:3,' ');
            writeln();
        end;
    end;
procedure swap1(var x,y:real);
    var
        z:real;
    begin
        z:=x;
        x:=y;
        y:=z;
    end;

procedure Transp(var a:ar;m:integer);
    var
        i,j:integer;
    begin
        for i:=0 to m-1 do
            for j:=i to m-1 do
                swap1(a[i,j],a[j,i]);
    end;

begin
    random;
    readln(m);
    setlength(mat,m);
    for i:=0 to m-1 do
        begin
            setlength(mat[i],m);
            for j:=0 to m-1 do
                mat[i,j]:=random(-20,20);
        end;
    outmat(mat,m);
    writeln();
    Transp(mat,m);
    outmat(mat,m);
end.