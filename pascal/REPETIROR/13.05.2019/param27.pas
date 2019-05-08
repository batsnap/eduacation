type
    matrix=array of array of real;
    ar=array of real;
var
    mat:matrix;
    j,i,m,n,k3,k4:integer;
    test:ar;
procedure sdvig(var a:ar;k1,k2:integer);
    var
        i,j:integer;
    begin
        j:=0;
        for i:=k1-1 to k2-1 do
            begin
                a[k1]:=a[k2-1+j];
                j+=1;
            end;
        setlength(a,n-(k2-k1));
    end;
procedure zapolnenie(var mat:matrix;m,n:integer);
    var
        i,j:integer;
    begin
        random;    
        setlength(mat,m);
        for i:=0 to m-1 do
            begin
                setlength(mat[i],n);
                for j:=0 to n-1 do
                    mat[i,j]:=random(-20,20);
            end;
    end;

procedure outmat(var a:matrix;m,n:integer);
    var
        i,j:integer;
    begin
        for i:=0 to m-1 do
        begin
            for j:=0 to n-1 do
                write(mat[i,j]:3,' ');
            writeln();
        end;
    end;
procedure RemoveCols(var a:matrix;m,n,k1,k2:integer);
    var
        i,j:integer;
    begin
        if k1<n-1 then
            if k2>n-1 then
                begin
                    k2:=n;
                    for i:=0 to m-1 do
                        sdvig(a[i],k1,k2);
                end
            else
                begin
                    for i:=0 to m-1 do
                        sdvig(a[i],k1,k2);
                end;
    end;

begin
    setlength(test,5);
    for i:=0 to 4 do
        test[i]:=real(i);
    writeln(test);
    {readln(m,n);}
    readln(k3,k4);
    sdvig(test,k3,k4);
    {zapolnenie(mat,m,n);
    outmat(mat,m,n);
    writeln();
    RemoveCols(mat,m,n,k1,k2);
    outmat(mat,m,n);}
end.