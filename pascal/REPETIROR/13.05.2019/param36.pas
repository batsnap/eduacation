var
    s:string;
    n,k:integer;
function InvertStr(var s:string;k,n:integer):string;
    var
        s1:string;
        i:integer;
    begin
        s1:='';
        if k>length(s) then 
            InvertStr:=''
        else
            begin
                if k+n-1>length(s) then
                    n:=length(s)-k+1;
                for i:=k+n-1 downto k do
                    s1:=s1+s[i];
            end;
        InvertStr:=s1;
end;
begin
    readln(s);
    readln(n,k);
    writeln(InvertStr(s,k,n));
end.