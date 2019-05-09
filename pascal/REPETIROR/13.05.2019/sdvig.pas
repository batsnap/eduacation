type
    ar=array of integer;
var
    i,k,k0:integer;
    a1:ar;
procedure sdvig(var a:ar;k1,k2:integer);
    var 
        i,j,s:integer;
        
    begin
        for j:=1 to k2-k1+1 do
            begin
                for i:=k1-1 to length(a)-2 do
                    a[i]:=a[i+1];
                setlength(a,length(a)-1)
            end;
    end;
begin
    readln(k,k0);
    setlength(a1,10);
    for i:=0 to 9 do
        a1[i]:=i;
    writeln(a1);
    sdvig(a1,k,k0);
    writeln(a1);
end.