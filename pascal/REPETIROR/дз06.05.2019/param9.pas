type
    ar=array of real;

var
    i,n:integer;
    a:ar;

procedure RemoveForInc(mas:ar;n:integer);
    var
        i,j:integer;
        x:real;
        b:ar;
    begin
        setlength(b,1);
        b[0]:=mas[0];
        x:=mas[0];
        j:=1;
        for i:=1 to n-1 do 
            begin
                if mas[i]>=x then
                    begin
                        j+=1;
                        setlength(b,j);
                        b[j-1]:=mas[i];
                    end;
                x:=mas[i];
            end;
        a:=b;
    end;

begin
    readln(n);
    setlength(a,n);
    for i:=0 to n-1 do
        readln(a[i]);
    RemoveForInc(a,n);
    writeln(a);
end.