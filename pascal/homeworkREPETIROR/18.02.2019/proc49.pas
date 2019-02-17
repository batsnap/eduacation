var a,b,c:integer;
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
function nod3(a,b,c:integer):integer;
    begin
        nod3:=nod2(nod2(a,b),c);
    end;

begin
read(a,b,c);
write(nod3(a,b,c));
end.