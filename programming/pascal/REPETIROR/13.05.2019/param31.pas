var
    s1:string;
    i,n:integer;
    x:boolean;

function fillstr(s:string;n:integer):string;
    var
        stroka:string;
        i:integer;
    begin
        stroka:='';
        while length(stroka)<n do
            stroka+=s;
        Delete(stroka,n+1,length(stroka)-N);
        fillstr:=stroka;
    end;
begin
    x:=true;
    readln(s1);
    readln(n);
    writeln(fillstr(s1,n))
end.