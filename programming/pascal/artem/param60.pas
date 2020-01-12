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

function DayInMonth(D:Tdate):integer;
var 
    a:integer;
begin
    if (D.month=2) and (LeapYear(D)) then
        DayInMonth:=29
    else if (D.month=2) then
        DayInMonth:=28
    else
        case D.month of
        1,3,5,7,8,10,12:DayInMonth:=31;
        2,4,6,9,11:DayInMonth:=30;
        else writeln('error');
end;
var
    a:Tdate;
begin
    readln(a.Day,a.Month,a.Year);
    writeln(DayInMonth(a));
end.