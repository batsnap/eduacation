var a,b:integer;
function nod2(a,b:integer):integer;
        begin
        repeat
            if a>b then
                a :=a mod b
            else
                b:=b mod a;
        until (a=0)or(b=0);
        nod2:=a+b;
    end;
procedure frac1(a,b:integer);
var c:integer;
begin
    c:=nod2(a,b);
    a:=a div c;
    b:=b div c;    
    writeln(a);
    writeln(b);
end;
begin
read(a,b);
frac1(a,b);
end.