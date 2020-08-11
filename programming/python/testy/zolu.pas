const N=2014; 
var  a : array [1..N] of integer; 
  i, j, s: integer; 
begin 
    for i:=1 to N do 
        readln(a[i]);
    s:=0;
    for i:=1 to N do
        begin 
        if (a[i]>99) and (a[i]<1000) and (a[i]mod 10=9) and (a[i] mod 100<>99) then
            s+=a[i];
        end;
    if s<>0 then
        writeln(s)
    else
        writeln(-1);
end.
