type train = record
n:string;
num:integer;
t:integer;
end;
var
a: array of string;
s:string;
i,j:integer;
begin
    setlength(a,10);
    a[0]:='v';
    a[1]:='s';
    for i:=2 to 10 do
        a[i]:='a';
    for i:=0 to 9 do
        for j:=0 to 8-i do
        begin
            if a[j]>a[j+1] then
                begin
                    s:=a[j];
                    a[j]:=a[j+1];
                    a[j+1]:=s;
                end;
        end;
    for i:=0 to 9 do
        writeln(a[i]);
end.