type Tdate=record
    Day:integer;
    Month:integer;
    Year:integer;
end;
function LeapYear(a:Tdate):boolean;
begin
    if ((a.Year mod 400=0) or ((a.Year mod 4=0) and (a.Year mod 100<>0))) then
        LeapYear:=True
    else
        LeapYear:=False;
end;
var
    Date:Tdate;
begin
    readln(Date.Day,Date.Month,Date.Year);
    writeln(LeapYear(Date));
end.