type train = record
tr:string;
num:integer;
t:integer;
end;

var a:array of train;
i,n,vr,j:integer;
s:string;
begin
  readln(n);
  setlength(a,n);
  for i:=0 to n-1 do 

      read(a[i].num,a[i].t,a[i].tr);


    for i:=0 to n-1 do 
      for j:=0 to n-1-i do

        if a[j].tr > a[j+1].tr  then
        begin
            s:=a[j].tr;
            a[j].tr:=a[j+1].tr;
            a[j+1].tr:=s;
        end;

    
    for i:=0 to n-1 do
        writeln(a[j].tr[0]);
end.